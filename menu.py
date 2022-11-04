from PIL import Image
import os

def select_img(directory):
    img = None
    print("Tamaño minimo: 103x103, Formato: PNG")
    print("Elements: ")
    arr = os.listdir("./" + directory)
    for element in arr:
        if element.lower().endswith(".png"):
            print(" - " + element)
    while img is None:
        try:
            direccion = input("\n¿Nombre de la imagen? (o refresh): ")
            direccion = directory + "/" + direccion
            img = Image.open(direccion)
        except:
            if direccion != directory + "/refresh":
                print("\nNombre o dirección erroneo!", end='')
            else:
                print("Elements: ")
                arr = os.listdir("./" + directory)
                for element in arr:
                    if element.lower().endswith(".png"):
                        print(" - " + element)
    return img, direccion

def mainmenu(options):
    text = input("Opciones: " + options[0] + ", " + options[1] + " o " + options[2] + ": ")
    text = text.lower()
    text = text.replace(' ', '')
    if options[0].find(text) == 0:
        return options[0]
    if options[1].find(text) == 0:
        return options[1]
    if options[2].find(text) == 0:
        return options[2]
    return ""