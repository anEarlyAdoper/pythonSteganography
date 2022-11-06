from random import randrange
import hashlib
import numpy
import numpy as np

def encripta(contrasena, mensaje, enter, string_separator, final_string):
    while not((len(mensaje)/8).is_integer()):
        mensaje= mensaje + enter
    #mensaje de 4 columnas y n filas
    msg_mat = np.zeros((8,int(len(mensaje)/8)))#filas, col
    aux = 0
    for fil in range(8):
        for col in range(int(len(mensaje) / 8)):
            msg_mat[fil][col]=ord(mensaje[aux])
            aux = aux + 1
    pass_mat = np.zeros((8,8))
    aux = 0
    for fil in range(8):
        for col in range(8):
            pass_mat[fil][col] = ord(contrasena[aux])
            aux = aux + 1
    sol = np.matmul(pass_mat, msg_mat)
    finalString = ""
    for fil in range(8):
        for col in range(int(len(mensaje) / 8)):
            finalString = finalString + str(int(sol[fil][col])) + string_separator
    finalString=finalString+final_string
    return finalString

def desencripta(contrasena, texto, string_separator):
    try:
        pass_mat = np.zeros((8, 8))
        aux = 0
        for fil in range(8):
            for col in range(8):
                pass_mat[fil][col] = ord(contrasena[aux])
                aux = aux + 1
        pass_mat=numpy.linalg.inv(pass_mat)
        aux = 0
        for x in texto:
            if x == string_separator:
                aux = aux + 1
        enc_mat = np.zeros((8, int(aux/8)))
        fil=0
        col=0
        combinacion=""
        for x in texto:
            if x == string_separator:
                enc_mat[fil][col] = int(combinacion)
                col = col + 1
                if col == int(aux / 8):
                    col = 0
                    fil = fil + 1
                combinacion = ""
            if x != string_separator:
                combinacion=combinacion+x
        msg_mat = np.matmul(pass_mat, enc_mat)
        mensaje = ""
        for fil in range(8):
            for col in range(int(aux/8)):
                mensaje = mensaje + chr(int(round(msg_mat[fil][col])))
        mensaje=mensaje.replace('\n','')
        return mensaje
    except:
        return None

def borrar(img, pixel, direccion):
    print("Cleaning image: ")
    donde = 1
    pixel_x = 0
    pixel_y = 0
    RGB = 0
    while pixel_x < img.size[0]:
        random = randrange(2)
        if RGB == 0:
            valor = pixel[pixel_x, pixel_y]
        valor_RGB = valor[RGB]
        valor_bin = '{0:08b}'.format(valor_RGB)
        valor_bin = valor_bin[:7] + str(random)
        aux = list(valor)
        aux[RGB] = int(valor_bin, 2)
        valor = tuple(aux)
        RGB = RGB + 1
        if RGB == 3:
            pixel[pixel_x, pixel_y] = valor
            RGB = 0
            pixel_y = pixel_y + 1
            if pixel_y == img.size[1]:
                if (pixel_x + 1) >= ((img.size[0] / 9) * donde):
                    print(str(donde*10) + "%")
                    donde = donde + 1
                pixel_y = 0
                pixel_x = pixel_x + 1
    print(str(donde*10) + "%")
    img.save(direccion)

def leer(offset, offset_x, offset_y,x,y, final_char, pixel, limit, n, img, string_separator):
    RGB = 0
    letra_int = 1
    extraido = ""
    print("Let's start reading\n")
    passw = input("Password for decrypting: ")
    encoded = passw.encode()
    offset[x] = ord(hashlib.sha256(encoded).hexdigest()[offset_x])
    offset[y] = ord(hashlib.sha256(encoded).hexdigest()[offset_y])
    pixel_x = offset[x]
    pixel_y = offset[y]
    while letra_int != ord(final_char):
        letra_bin = ""
        while len(letra_bin) != 8:
            if RGB == 0:
                valor = pixel[pixel_x, pixel_y]
            valor_RGB = valor[RGB]
            valor_bin = '{0:08b}'.format(valor_RGB)
            letra_bin = letra_bin + valor_bin[7]
            RGB = RGB + 1
            if RGB == 3:
                #print("Leemos en x: " + str(pixel_x) + " y: " + str(pixel_y))
                RGB = 0
                limit[y] = limit[y] + 1
                pixel_y = pixel_y + offset[y]
                if pixel_y >= img.size[y]:
                    n[y] = n[y] + 1
                    pixel_y = offset[y] - n[y]
                if limit[y] == img.size[y]:
                    n[y] = 0
                    limit[y] = 0
                    pixel_x = pixel_x + offset[x]
                    limit[x] = limit[x] + 1
                if pixel_x >= img.size[x]:
                    n[x] = n[x] + 1
                    pixel_x = offset[x] - n[x]
                if limit[x] == img.size[x]:
                    print("Error: Out of range")
                    exit()
        letra_int = int(letra_bin, 2)
        if letra_int != ord(final_char):
            letra = chr(letra_int)
            extraido = extraido + letra
    extraido = desencripta(hashlib.sha256(encoded).hexdigest(), extraido, string_separator)
    return extraido

def guardar(img, pixel, offset, offset_x, offset_y, enter, string_separator, final_string,x,y, limit, n, direccion):
    print("Let's save some text\n")
    passw = input("Introduce password for encryption: ")
    while passw == "":
        print("You have to type a password")
        passw = input("Introduce password for encryption: ")
    mensaje = input("Introduce the message to be saved (the message can't have the character 'enter'): ")
    encoded = passw.encode()
    mensaje = encripta(hashlib.sha256(encoded).hexdigest(), mensaje, enter, string_separator, final_string)
    offset[x] = ord(hashlib.sha256(encoded).hexdigest()[offset_x])
    offset[y] = ord(hashlib.sha256(encoded).hexdigest()[offset_y])
    pixel_x = offset[x]
    pixel_y = offset[y]
    mensaje_ascii = []
    donde = 1
    RGB = 0
    used = 0
    print("Encrypting:  ")
    for character in mensaje:
        mensaje_ascii.append(ord(character))
    for letter in mensaje_ascii:
        binary = '{0:08b}'.format(letter)
        if (used + 1) >= ((img.size[x]*img.size[y] / 9) * donde):
            print(str(donde*10) + "%")
            donde = donde + 1
        for bit in binary:
            if RGB == 0:
                valor = pixel[pixel_x, pixel_y]
            valor_RGB = valor[RGB]
            valor_bin = '{0:08b}'.format(valor_RGB)
            valor_bin = valor_bin[:7] + bit
            aux = list(valor)
            aux[RGB] = int(valor_bin, 2)
            valor = tuple(aux)
            RGB = RGB + 1
            if RGB == 3:
                used = used + 1
                pixel[pixel_x, pixel_y] = valor
                RGB = 0
                pixel_y = pixel_y + offset[y]
                limit[y] = limit[y] + 1
                if pixel_y >= img.size[y]:
                    n[y] = n[y] + 1
                    pixel_y = offset[y] - n[y]
                if limit[y] == img.size[y]:
                    n[y] = 0
                    limit[y] = 0
                    pixel_x = pixel_x + offset[x]
                    limit[x] = limit[x] + 1
                if pixel_x >= img.size[x]:
                    n[x] = n[x] + 1
                    pixel_x = offset[x] - n[x]
                if limit[x] == img.size[x]:
                    print("Error: Out of range, the text you are trying to save is too big.")
                    exit()
    cual = used
    while cual < img.size[x]*img.size[y]:
        if (cual + 1) >= ((img.size[x]*img.size[y] / 9) * donde):
            print(str(donde*10) + "%")
            donde = donde + 1
        random = randrange(2)
        if RGB == 0:
            valor = pixel[pixel_x, pixel_y]
        valor_RGB = valor[RGB]
        valor_bin = '{0:08b}'.format(valor_RGB)
        valor_bin = valor_bin[:7] + str(random)
        aux = list(valor)
        aux[RGB] = int(valor_bin, 2)
        valor = tuple(aux)
        RGB = RGB + 1
        if RGB == 3:
            cual = cual + 1
            pixel[pixel_x, pixel_y] = valor
            RGB = 0
            pixel_y = pixel_y + offset[y]
            limit[y] = limit[y] + 1
            if pixel_y >= img.size[y]:
                n[y] = n[y] + 1
                pixel_y = offset[y] - n[y]
            if limit[y] == img.size[y]:
                n[y] = 0
                limit[y] = 0
                pixel_x = pixel_x + offset[x]
                limit[x] = limit[x] + 1
            if pixel_x >= img.size[x]:
                n[x] = n[x] + 1
                pixel_x = offset[x] - n[x]
    img.save(direccion)
    print(str(donde*10) + "%")
    return used
