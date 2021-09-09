'''
Se pide hacer un programa que abra un archivo de texto llamado entrada.txt 
el mismo contiene el siguiente poema de Ruben Dario:

...

Y permita al usuario poder buscar palabras. Si las mismas se encuentran deberá:

    a - indicar cuántas veces aparece y en qué línea del poema está.
    b - copiar la línea a un archivo llamado salida.txt

Además se deberá implementar try except para la apertura de archivos
'''

from io import TextIOWrapper
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
NOMBRE_ARCHIVO_ENTRADA = "entrada.txt"
RUTA_ARCHIVO_ENTRADA = os.path.join(BASE_DIR, NOMBRE_ARCHIVO_ENTRADA)

NOMBRE_ARCHIVO_SALIDA = "salida.txt"
RUTA_ARCHIVO_SALIDA = os.path.join(BASE_DIR, NOMBRE_ARCHIVO_SALIDA)


def buscar_palabras(poema: TextIOWrapper, ruta_archivo_salida: str) -> None:
    contador_lineas = 0
    palabra_apariciones = 0
    palabra_apariciones_lineas = list()

    palabra = input("Ingrese la palabra que desea buscar >>>   ")

    for linea in poema:
        contador_lineas += 1
        if palabra.lower() in linea:
            palabra_apariciones += 1
            palabra_apariciones_lineas.append(contador_lineas)
            with open(ruta_archivo_salida, 'a') as salida: salida.write(linea)

    if palabra_apariciones > 0:
        print(f"La palabra '{palabra.upper()}' aparece {palabra_apariciones} veces en el poema, en las líneas", end=" ")
        for i in range(len(palabra_apariciones_lineas)): print(palabra_apariciones_lineas[i], end=", ")
    else:
        print(f"La palabra '{palabra.upper()}' no aparece en el poema")


def main() -> None:
    with open(RUTA_ARCHIVO_ENTRADA, 'r') as poema:
        buscar_palabras(poema, RUTA_ARCHIVO_SALIDA)


main()
