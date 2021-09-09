
def maximo(numeros: list) -> float:
    max_iniciador = False; maximo = 0

    for i in range(len(numeros)):
        if max_iniciador == False:
            maximo = numeros[i]
            max_iniciador = True
        
        if numeros[i] >= maximo:
            maximo = numeros[i]
    
    return maximo


def minimo(numeros: list) -> float:
    min_iniciador = False; minimo = 0

    for i in range(len(numeros)):
        if min_iniciador == False:
            minimo = numeros[i]
            min_iniciador = True
        
        if numeros[i] <= minimo:
            minimo = numeros[i]
    
    return minimo


def promedio(numeros: list) -> float:
    acumulador = 0

    for i in range(len(numeros)):
        acumulador += numeros[i]

    try:
        return acumulador/len(numeros)
    except ZeroDivisionError:
        return 0


def ingresar_lista_numeros(cantidad_numeros: int = 0) -> list:
    lista_numeros = list()
    seguir_ingresando = True

    if cantidad_numeros == 0:
        while seguir_ingresando:
            numero = input("Ingrese un numero o 's' para terminar:  ")
            es_numero = True

            if numero == 's':
                seguir_ingresando = False
            else:
                try:
                    float(numero)
                except ValueError:
                    es_numero = False
                    print("No se ha ingresado un número")
                
                if es_numero: 
                    lista_numeros.append(float(numero))
                    print(f"Ha ingresado el numero: {numero}")
    else:
        if cantidad_numeros > 0:
            i = 0

            while i < cantidad_numeros:
                numero = input(f"Ingrese el numero {i + 1}/{cantidad_numeros}:  ")
                es_numero = True

                try:
                    float(numero)
                except ValueError:
                    es_numero = False
                    print("No se ha ingresado un número")
                
                if es_numero: 
                    lista_numeros.append(float(numero))
                    i += 1 
                    print(f"Ha ingresado el numero: {numero}")
        else:
            print("La cantidad de numeros a ingresar establecida no es mayor a cero.")

    return lista_numeros


def borrar_decimales_cero(numero: float, redondear: bool = False) -> str:
    
    if float(str(numero).split(".")[1]) == 0:
        return round(numero)  # 123.00  -->>  ['123', '00']  -->>  123
    else:
        if redondear: 
            return round(numero, 2)  # 123.45129  -->>  123.45
        else: 
            return numero


def main() -> None:
    lista_numeros = ingresar_lista_numeros()

    numero_max = borrar_decimales_cero(maximo(lista_numeros))
    numero_min = borrar_decimales_cero(minimo(lista_numeros))
    numero_pro = borrar_decimales_cero(promedio(lista_numeros), True)

    print(f"\n\nEl número más grande de la lista es: {numero_max}")
    print(f"\nEl número más chico de la lista es: {numero_min}")
    print(f"\nEl promedio de todos los números de la lista es: {numero_pro}")


main()
