'''
Números escalonados: Un número es escalonado, si sus dígitos están en orden estrictamente creciente.

Por ejemplo, 359 es escalonado, 34 también, pero 5674 no es, y tampoco 5667.
Se recibe un número entero por parámetro N > 10 (lo cual se debe validar).
La salida debe decir si es un número escalonado o no lo es y a continuación indicar la cantidad de dígitos cuya secuencia
fue escalonada.

Datos de entrada:
Se recibe un parámetro con el número entero N.

Datos de salida:
El programa debe imprimir por pantalla en una línea, conteniendo un único número: la cantidad de números
escalonados que hay entre 10 y N, inclusive.

Ejemplo1: Entrada: 359 - Salida: “Es escalonado”, 3
Ejemplo2: Entrada: 24893471 - Salida: “No es escalonada”, 4
'''


def numero_escalonado(numero: int) -> None:
    numero_digitos = list()

    numero = str(numero)

    for digito in numero:
        numero_digitos.append(int(digito))
    
    escalonado = True
    contador_escalonados = 1
    contar_escalonados = True

    for i in range(1, len(numero_digitos)):
        if numero_digitos[i] <= numero_digitos[i - 1]:
            escalonado = False
            contar_escalonados = False
        else:
            if contar_escalonados:
                contador_escalonados += 1
    
    if escalonado: print('"Es escalonado",', contador_escalonados) 
    else: print('"No es escalonada",', contador_escalonados)


def main() -> None:
    numero = 0

    while numero <= 10:
        numero = int(input("Ingrese un numero entero mayor a 10:  "))
    
    numero_escalonado(numero)


main()
