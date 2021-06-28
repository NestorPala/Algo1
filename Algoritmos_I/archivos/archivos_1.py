
def leer_archivo(ruta_archivo: str, modo: int) -> None:
    if modo == 1:
        # Este bucle abre, lee y cierra el archivo
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                # Cada linea es una lista, en este caso imprimimos el primer elemento de cada linea
                print(linea[0])

                # linea = linea.rstrip("\n")
                # print
    elif modo == 2:
        # Abrimos el archivo
        archivo = open(ruta_archivo, 'r')

        # Leemos el archivo
        for linea in archivo:
                print(linea[0])

        # Cerramos el archivo
        archivo.close()


def sumar_numeros(ruta_archivo_2: str) -> int:
    suma = 0

    with open(ruta_archivo_2, 'r') as archivo:
        for linea in archivo:
            suma += int(linea)
    
    return suma


def main():
    ruta_archivo = "cadenas.txt"
    leer_archivo(ruta_archivo, 2)

    ruta_archivo_2 = "numeros.txt"

    # Sirve para comprobar errores (tira una excepción)
    assert(sumar_numeros(ruta_archivo_2) == 2613600)
    

main()
