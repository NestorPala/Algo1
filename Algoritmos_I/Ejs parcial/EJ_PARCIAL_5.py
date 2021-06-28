'''

5) Escribir un programa que primero solicite una palabra al usuario y luego le permita al usuario ingresar 5 palabras.
    El sistema deberá calcular cuántas y cuáles palabras de las 5 ingresadas pueden escribirse exactamente con las letras 
    de la palabra ingresada al principio (utilizando todas las letras y sin repetir ninguna).
    Ej: Palabra inicial: CASO
        5 palabras: MAMA, CLASE, SACO, COSA, PEPE
    EL sistema deberá devolver 2 palabras (SACO y COSA).

'''
def extraer_anagramas(palabra: str, palabras: list) -> list:
    letras_palabra = list()
    letras_palabra_contadas = list()

    for elemento in palabra:
        letras_palabra.append(elemento)
    
    for elemento in letras_palabra:
        letras_palabra_contadas.append([elemento, letras_palabra.count(elemento)])
    
    #...

    anagramas = list()


def main() -> None:
    palabras = list()

    palabra = input("Ingrese una palabra >>>   ")

    for i in range(5):
        p1 = input(f"Ingrese una nueva palabra {i} >>>   ")
        palabras.append(p1)

    anagramas = extraer_anagramas(palabra, palabras)
    print(f"Los anagramas de '{palabra}' en la lista {palabras} son {anagramas}")


main()