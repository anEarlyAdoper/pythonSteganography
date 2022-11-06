import sys

from menu import mainmenu
from menu import select_img

from operations import guardar
from operations import borrar
from operations import leer

#define
directory = "images"
version = "1.0"
x=0
y=1
enter = '\n'
string_separator = '&'
final_string = '!!!!!'
final_char='!'
offset=[0,0]
limit=[0,0]
n=[0,0]
offset_x=16
offset_y=17
options=["save", "read", "delete content"]
#end define

def main():
    print("¡Welcome! v" + version + "\n")
    img, direccion = select_img(directory)

    if (img.size[0] <= 103 or img.size[1] <= 103):
        print("La image is to small")
        exit()

    if not (direccion.find(".png") != -1 or direccion.find(".PNG") != -1):
        print("Wrong image format, is not PNG")
        exit()

    print("\nImage size: " + str(img.size) + "\n")

    respuesta = mainmenu(options)
    while respuesta == '':
        print("ERROR value\n")
        respuesta = mainmenu(options)

    pixel = img.load()

    if respuesta == options[2]:
        try:
            borrar(img, pixel, direccion)
            print("\nCleaned ok!\n")
        except:
            print("Error: " + str(sys.exc_info()[0]))

    if respuesta == options[1]:
        try:
            extraido = leer(offset, offset_x, offset_y, x, y, final_char, pixel, limit, n, img, string_separator)
            if extraido == "" or extraido == "\n":
                print("Error decrypting: wrong password.")
            else:
                print("Readed message: " + extraido)
        except:
            print("Error decrypting: wrong password.")

    if respuesta == options[0]:
        try:
            used = guardar(img, pixel, offset, offset_x, offset_y, enter, string_separator, final_string, x, y, limit,
                           n, direccion)
            print("\nSaved correctly!\n")
            tamano_usado = "{:.2f}".format(100 * (used / (img.size[0] * img.size[1])) * 1.0)
            print("Used space: " + str(tamano_usado) + "%")
        except:
            print("Error: " + str(sys.exc_info()[0]))
    input("\npress 'Enter' to exit.")

if __name__ == "__main__":
    main()