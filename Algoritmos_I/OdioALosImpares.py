'''
(El ejercicio se llama: ODIO A LOS IMPARES)

Crear un programa que:

- Permita ingresar 5 números enteros positivos.
- Calcule el máximo entre esos números; lo muestre.
- Calcule el mínimo; lo muestre.
- Calcule el promedio; lo muestre.

- Sume el máximo, el mínimo; y el promedio
(Resultando en un entero. Para eso pueden castear el resultado a int. Ejemplo: int(resultado)) y en caso de que el resultado sea par;
salude al usuario tantas veces como número resultante de esa cuenta, si es impar; vuelve a empezar TODO el programa DE NUEVO.
'''

CANT_ENTEROS_POSITIVOS = 5


def sumaloca_saludo() -> bool:
    acumulador = 0
    min_max_iniciador = False
    
    print("INGRESE 5 NUMEROS POSITIVOS")
    
    for i in range(CANT_ENTEROS_POSITIVOS):
        ingreso = input((f"INGRESE NUMERO {i+1}:   "))
        
        while not (ingreso.isnumeric() and int(ingreso) > 0):
            ingreso = input("INGRESE UN NUMERO POSITIVO:   ")
        
        numero = int(ingreso)
        
        if min_max_iniciador == False:
            minimo = numero
            maximo = numero
            min_max_iniciador = True
        
        if numero < minimo:
            minimo = numero
        
        if numero > maximo:
            maximo = numero
            
        acumulador += numero
    
    promedio = acumulador / CANT_ENTEROS_POSITIVOS
    sumaloca = int(minimo + maximo + promedio)
    print(minimo, maximo, promedio)
    print("LA SUMA DEL MAXIMO, DEL MINIMO Y DEL PROMEDIO ES:", sumaloca)
    
    if sumaloca % 2 == 0:
        for i in range(sumaloca):
            print("¡HOLA, COMO ESTÁS MÁQUINA, FIERA, TITÁN, PAPURRI, ÍDOLO, MÁSTER, CAPO, CRACK, TIFÓN, LOCURA!")
        impares_todo_mal = False
    else:
        impares_todo_mal = True
        
    return impares_todo_mal


def main() -> None:
    impares = True
    while impares:
        impares = sumaloca_saludo()


main()