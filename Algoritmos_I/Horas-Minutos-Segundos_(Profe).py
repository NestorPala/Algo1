CANT_INTERVALOS = 2
def convertir_a_segundos(hora : int, minuto : int, segundo : int) -> int:
    '''
    PRE: hora, minuto y segundo sean un numero > 0
    POST: Devuelve la suma en segundos
    '''
    return (hora*3600 + minuto*60 + segundo)
def convertir_a_formato(total : int) -> tuple:
    '''
    PRE: total sea un numero > 0
    POST: Devuelve una tupla con total divido en (horas, minutos, segundos)
    '''
    hora = (total // 3600)
    minutos = (total % 3600) // 60
    segundos = (total % 60)
    return hora,minutos,segundos
def ingresar_intervalo() -> int:
    '''
    PRE: -
    POST: Devuelve una tupla con (horas, minutos, segundos)
    '''
    hora = input("Ingresar hora: ")
    while not (hora.isnumeric() and int(hora) >= 0):
        hora = input("Error! Ingrese un valor válido: ")
    minuto = input("Ingrese minutos: ")
    while not (minuto.isnumeric() and int(minuto) >= 0 and int(minuto) < 60):
        minuto = input("Error! Ingrese un valor válido: ")
    segundo = input("Ingrese segundos: ")
    while not (segundo.isnumeric() and int(segundo) >= 0 and int(segundo) < 60):
        segundo = input("Error! Ingrese un valor válido: ")
    print(f"\n\n Ingresó la hora {hora}:{minuto}:{segundo}\n\n")
    return int(hora), int(minuto), int(segundo)
def main() -> None:
    suma = 0
    for i in range(CANT_INTERVALOS):
        print(f"\t\tDATOS DE INTERVALO {i+1}")
        horas, minutos, segundos = ingresar_intervalo()
        suma += convertir_a_segundos(horas, minutos, segundos)
    horas, minutos, segundos = convertir_a_formato(suma)
    print(f"La suma de los tiempos da {horas}:{minutos}:{segundos}")
main()