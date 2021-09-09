
'''
Observe la siguiente secuencia: 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 cada número de la misma se ha obtenido 
como la mitad del anterior si éste era par o el triple más uno si era impar. Por ejemplo, el 34 es par, 
luego le sigue el 17 que es su mitad; el 5 es impar, luego le sigue su triple 15 aumentado en 1 o sea 16.

El número que encabeza la secuencia lo denominamos semilla de la misma, en este caso el 22. 
Hay un matemático que quiere estudiarla y pide tu ayuda. Existe la conjetura de que estas secuencias, 
cualquiera sea la semilla llegará a 1.

A pesar de la simplicidad de la regla de formación no ha sido demostrada, 
pero sí ensayada para gran cantidad de números de modo tal que 
para las semillas que ensayará el matemático lo puedes dar por cierto: la secuencia termina con un uno, 
ya que después repite valores. Al matemático le interesa averiguar en cada ensayo para una semilla dada,

a) ¿Cuán larga es la secuencia?
b) ¿Cuál es el número más grande que contiene?
c) ¿Cuál es el promedio de la secuencia?
d) ¿Mostrar todos los números que sean mayor o igual a 23? 
'''


def maximo(numeros: list) -> int:
    max_iniciador = False; maximo = 0

    for i in range(len(numeros)):
        if max_iniciador == False:
            maximo = numeros[i]
            max_iniciador = True
        
        if numeros[i] >= maximo:
            maximo = numeros[i]
    
    return maximo


def promedio(numeros: list) -> float:
    acumulador = 0

    for i in range(len(numeros)):
        acumulador += numeros[i]

    return acumulador/len(numeros)


def mayor_igual(numeros: list, piso: int) -> list:
    resultado = list()

    for i in range(len(numeros)):
        if numeros[i] >= piso:
            resultado.append(numeros[i])
    
    return(resultado)


def secuencia_loca(semilla: int) -> list:
    resultado = list()
    numero = 0

    while numero != 1:
        if numero == 0:
            numero = semilla
            resultado.append(numero)
        
        if numero % 2 == 0:
            numero = numero // 2
            resultado.append(numero)
        else:
            numero = numero * 3 + 1
            resultado.append(numero)
    
    return resultado


def main() -> None:
    semilla = int(input("INGRESE UNA SEMILLA: "))
    secuencia = secuencia_loca(semilla)

    print("Se ha generado la secuencia.")
    print(f"El largo de la secuencia (con la semilla) es: {len(secuencia)}")
    print(f"El número más grande de la secuencia es: {maximo(secuencia)}")
    print(f"El promedio de la secuencia es: {promedio(secuencia)}")
    print(f"Los números mayores o iguales a 23 son: {mayor_igual(secuencia, 23)}")


main()
