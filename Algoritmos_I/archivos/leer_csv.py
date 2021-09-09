import csv


def cargar_archivo(ruta: str) -> None:

    with open (ruta, 'r', encoding="UTF-8", newline='') as archivo_csv:
        contenido_csv = csv.reader(archivo_csv, delimiter= ';')
        #next(csv_reader)   #SI EL CSV TIENE HEADER

        for fila in contenido_csv:
            provincia = fila[1]
            print(provincia)

        '''
        #AGREGAR DATOS CSV A DICCIONARIO
        for fila in contenido_csv:
            diccionario[fila[0]] = (fila[1], fila[2])
        '''


ruta = 'ciudades.csv'
cargar_archivo(ruta)



