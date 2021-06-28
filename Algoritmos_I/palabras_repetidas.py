'''
Se solicita crear una función en la cual reciba un texto(string) como parámetro,
y que devuelva un diccionario con las palabras como clave y como valor la cantidad de veces que 
se repite dicha palabra, a modo de ejemplo, dado el siguiente texto:
    Auto Casa Avion Auto casa casa
la función deberá devolver el siguiente diccionario:
    {"Auto":2, "Casa":1, "Avion":1, "casa":2}
Una vez se haya implementado la función, se solicita crear otra función que en vez de contar 
cada palabra, cuente cada letra, es decir que del texto anterior debe salir el sig. diccionario:
    {'A': 3, 'u': 2, 't': 2, 'o': 3, 'C': 1, 'a': 6, 's': 3, 'v': 1, 'i': 1, 'n': 1, 'c': 2}
'''

def generar_diccionario_palabras(palabras: str) -> None:
    diccionario_palabras = dict()
    palabras_lista = palabras.split(" ")
    
    for i in range(len(palabras_lista)):
        diccionario_palabras[palabras_lista[i]] = palabras_lista.count(palabras_lista[i])
    
    print(diccionario_palabras)


def generar_diccionario_letras(palabras: str) -> None:
    diccionario_palabras = dict()
    
    for i in range(len(palabras)):
        diccionario_palabras[palabras[i]] = palabras.count(palabras[i])
    
    print(diccionario_palabras)


def main() -> None:
    a = input("Ingrese palabras separadas por espacios hasta que se aburra >>> ")
    generar_diccionario_palabras(a)
    generar_diccionario_letras(a)


main()