'''
ejercicio de parcial!

3)  Se pide realizar una función que devuelva el número entero más pequeño de un listado ingresado por el usuario, 
    tal que la suma de los N números exceda un valor pasado por parámetro en la función.

    def Funcion(valorLimite int):
     #El usuario ingrese n valores entreros hasta que la sumatoria de los mismos sea igual o menor al valorLimite

    return valorMinimo
'''


def listado_numeros(valor_limite: int) -> int:
    minimo = 0
    acumulador = 0
    min_iniciador = False

    while int(acumulador) <= int(valor_limite):
        numero = input(f"Ingrese numeros hasta que su suma exceda {valor_limite} >>> ")
        acumulador += int(numero)

        if min_iniciador == False:
            minimo = int(numero)
            min_iniciador = True

        if int(numero) < int(minimo):
            minimo = int(numero)

    return minimo


def main() -> None:
    numero = input("Ingrese un numero >>> ")
    minimo = listado_numeros(numero)
    print(f"El numero mas chico de la lista recien ingresada es: {int(minimo)}")
    

main()