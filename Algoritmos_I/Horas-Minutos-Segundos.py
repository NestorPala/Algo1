CANTIDAD_INTERVALOS = 2


def calcular_segundos(horas: int, minutos: int, segundos: int) -> int:
    return horas*3600 + minutos*60 + segundos

def formatear_segundos(segs: int) -> tuple:
    horas = segs // 3600
    minutos = (segs % 3600) // 60
    segundos = segs % 60
    return horas, minutos, segundos

def main() -> None:
    suma_intervalos = 0
    for i in range(CANTIDAD_INTERVALOS):
        
        horas = input(f"INGRESE HORAS INTERVALO {i+1}: ")
        while not (horas.isnumeric() and int(horas) < 24):
            horas = input("INGRESE UNA CANTIDAD DE HORAS ENTRE 0 Y 23:   ")
        
        minutos = input(f"INGRESE MINUTOS INTERVALO {i+1}: ")
        while not (minutos.isnumeric() and int(minutos) < 60):
            minutos = input("INGRESE UNA CANTIDAD DE MINUTOS ENTRE 0 Y 59:   ")
            
        segundos = input(f"INGRESE SEGUNDOS INTERVALO {i+1}: ")
        while not (horas.isnumeric() and int(segundos) < 60):
            segundos = input("INGRESE UNA CANTIDAD DE SEGUNDOS ENTRE 0 Y 59:   ")
        
        suma_intervalos += calcular_segundos(int(horas), int(minutos), int(segundos))
    
    horas, minutos, segundos = formatear_segundos(suma_intervalos)
    
    print(f"LA SUMA DE LOS DOS INTERVALOS ES: {horas}:{minutos}:{segundos}")


main()