import sys

from menu import mainmenu
from menu import select_img

from operations import guardar
from operations import borrar
from operations import leer

#define
directory = "images"
version = "1.2"
audio_name = "audio/audio.mp3"
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
options=["guardar", "leer", "borrar contenido"]
#end define

def main():
    print("¡Bienvenido! v" + version + "\n")
    img, direccion = select_img(directory)

    if (img.size[0] <= 103 or img.size[1] <= 103):
        print("La imagen es demasiado pequeña")
        exit()

    if not (direccion.find(".png") != -1 or direccion.find(".PNG") != -1):
        print("Formato de la imagen erroneo, no es PNG")
        exit()

    print("\nEl tamaño de la imagen es de " + str(img.size) + "\n")

    respuesta = mainmenu(options)
    while respuesta == '':
        print("ERROR value\n")
        respuesta = mainmenu(options)

    pixel = img.load()

    if respuesta == options[2]:
        try:
            borrar(img, pixel, direccion, audio_name)
            print("\nLimpiado finalizado con exito!\n")
        except:
            print("Error: " + str(sys.exc_info()[0]))

    if respuesta == options[1]:
        try:
            extraido = leer(offset, offset_x, offset_y, x, y, final_char, pixel, limit, n, img, string_separator)
            if extraido == "" or extraido == "\n":
                print("Error al descodificar.")
            else:
                print("Mensaje leido: " + extraido)
        except:
            print("Error al descodificar.")

    if respuesta == options[0]:
        try:
            used = guardar(img, pixel, offset, offset_x, offset_y, enter, string_separator, final_string, x, y, limit,
                           n, direccion)
            print("\nGuardado correctamente!\n")
            tamano_usado = "{:.2f}".format(100 * (used / (img.size[0] * img.size[1])) * 1.0)
            print("Espacio usado: " + str(tamano_usado) + "%")
        except:
            print("Error: " + str(sys.exc_info()[0]))

    input("\npresiona 'Enter' para salir.")

if __name__ == "__main__":
    main()

