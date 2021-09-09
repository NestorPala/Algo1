import csv
import os
from pathlib import Path


RUTA_ALUMNOS_CSV = f"{Path.home()}\\Desktop\\alumnos.csv"
RUTA_MATERIAS_CSV = f"{Path.home()}\\Desktop\\materias.csv"


def ingresar_opcion(rango_opciones: int) -> int:

    opcion = input(">>> Ingrese la opción:   ")
    
    while not (opcion.isnumeric() and 0 < int(opcion) <= rango_opciones):
        if rango_opciones == 1:
            opcion = input("Pulse 1 >>>   ")
        else:
            opcion = input(f"Ingrese una opcion entre 1 y {rango_opciones} >>>   ")

    return int(opcion)


def limpiar_pantalla() -> None:
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def alta_alumnos(alumnos: dict, materias: dict) -> None:
    print(f"Obteniendo información de los alumnos desde {RUTA_ALUMNOS_CSV} ...")

    with open(RUTA_ALUMNOS_CSV, mode = 'r', encoding = "utf-8") as archivo_csv:
        csv_reader = csv.reader(archivo_csv, delimiter = ';')
        next(csv_reader)

        for fila in csv_reader:
            padron = int(fila[0])

            alumnos[padron] = dict()
            alumnos[padron]["nombre"] = fila[1]
            alumnos[padron]["apellido"] = fila[2]
            alumnos[padron]["carrera"] = fila[3]
            alumnos[padron]["anio_ingreso"] = int(fila[4])

    print(f"Obteniendo información de las materias de cada alumno desde {RUTA_MATERIAS_CSV} ...")

    with open(RUTA_MATERIAS_CSV, mode = 'r', encoding = "utf-8") as archivo_csv:
        csv_reader = csv.reader(archivo_csv, delimiter = ';')
        next(csv_reader)

        for fila in csv_reader:
            padron = int(fila[0])
            materias[padron] = dict()
            materias_notas = list()

            for i in range(len(fila)):
                materias_notas.append(fila[i])

            materias_notas.pop(0)

            for i in range(len(fila)):
                if i % 2 == 1:
                    materias[padron][fila[i]] = int(fila[i + 1])

    input("Información cargada al sistema. Presione una tecla para continuar... ")


def ingresar_anio() -> int:
    anio = " "

    while not anio.isnumeric() and not len(anio) == 4:
        anio = input("Ingrese el año actual para calcular antigüedad:  ")
    
    return int(anio)


def promedio(lista_numeros: list) -> int:
    total = 0

    for i in range(len(lista_numeros)):
        total += lista_numeros[i]

    return int(total / len(lista_numeros))


def antiguedad_promedio_carrera(alumnos: dict) -> None:
    fecha_actual = ingresar_anio()

    #carrera_antiguedad_aux = {nombre_carrera: [años_alumno1, años_alumno2, etc.]}
    carrera_antiguedad_aux = dict()

    #carrera_antiguedad = {nombre_carrera: antiguedad}
    carrera_antiguedad = dict()

    for alumno in alumnos:
        carrera_aux = alumnos[alumno]["carrera"]
        antiguedad_aux = fecha_actual - int(alumnos[alumno]["anio_ingreso"])
    
        if carrera_aux not in carrera_antiguedad_aux:
            carrera_antiguedad_aux[carrera_aux] = [antiguedad_aux]
        else:
            carrera_antiguedad_aux[carrera_aux].append(antiguedad_aux)
    
    for carrera in carrera_antiguedad_aux:
        carrera_antiguedad[carrera] = promedio(carrera_antiguedad_aux[carrera])

    print(f"Fecha actual: {fecha_actual}")
    print("Lista de antigüedad promedio de alumnos en cada carrera según cantidad de años")

    for carrera in carrera_antiguedad:
        print(f"{carrera} - {carrera_antiguedad[carrera]}")
    
    input("Presione una tecla para continuar...  ")


def mejor_alumno_facultad(alumnos: dict, materias: dict) -> None:
    # notas_alumnos_aux = {padron: [nota1, nota2, nota3, etc.]}
    notas_alumnos_aux = dict()

    # notas_alumnos = {padron: nota_promedio}
    notas_alumnos = dict()

    for padron in alumnos:
        notas_alumnos_aux[padron] = list()

        for materia in materias[padron]:
            nota = materias[padron][materia]
            notas_alumnos_aux[padron].append(nota)
    
    for padron in notas_alumnos_aux:
        notas_alumnos[padron] = promedio(notas_alumnos_aux[padron])

    nota_max = 0; padron_max = 0
    max_iniciador = False

    for padron in notas_alumnos:
        if max_iniciador == False:
            nota_max = notas_alumnos[padron]
            max_iniciador = True
        
        if notas_alumnos[padron] >= nota_max:
            nota_max = notas_alumnos[padron]
            padron_max = padron
    
    alumno_mejor_promedio = f"{alumnos[padron_max]['apellido']}, {alumnos[padron_max]['nombre']}"

    print(f"El promedio de notas más alto de la facultad es: \n  {alumno_mejor_promedio} \n con: {nota_max} puntos")
    input("Presione una tecla para continuar...  ")


def promedio_materias_aprobadas_carrera(alumnos: dict, materias: dict) -> None:
    carrera = input("Ingrese la carrera de la cual desea ver el promedio de materias aprobadas:  ")

    # materias_aprobadas_carrera_aux = [cantidad_aprobados_alumno1, cantidad_aprobados_alumno2, etc.]
    materias_aprobadas_carrera_aux = list()

    for padron in alumnos:
        if alumnos[padron]["carrera"] == carrera:
            cantidad_materias_aprobadas = 0

            for materia in materias[padron]:
                nota = materias[padron][materia]
                if nota >= 4:
                    cantidad_materias_aprobadas += 1
        
        materias_aprobadas_carrera_aux.append(cantidad_materias_aprobadas)
    
    materias_aprobadas_carrera = promedio(materias_aprobadas_carrera_aux)

    print(f"El promedio de materias aprobadas en la carrera '{carrera}' es: {materias_aprobadas_carrera}")
    input("Presione una tecla para continuar...  ")


def departamento_mas_aprobados(alumnos: dict, materias: dict) -> None:
    # departamento_materias_aprobadas = {id_departamento: cantidad_materias_aprobadas}
    departamento_materias_aprobadas = dict()

    for padron in alumnos:
        for materia in materias[padron]:
            departamento = materia.split(".")[0]
            nota = materias[padron][materia]
            if nota >= 4:
                if departamento not in departamento_materias_aprobadas:
                    departamento_materias_aprobadas[departamento] = 1
                else:
                    departamento_materias_aprobadas[departamento] += 1

    maximo = 0
    departamento_maximo = " "
    max_iniciador = False

    for departamento in departamento_materias_aprobadas:
        if not max_iniciador:
            maximo = departamento_materias_aprobadas[departamento]
            departamento_maximo = departamento
            max_iniciador = True
        
        if departamento_materias_aprobadas[departamento] >= maximo:
            maximo = departamento_materias_aprobadas[departamento]
            departamento_maximo = departamento

    print(f"El departamento con más aprobados es: '{departamento_maximo}' con {maximo} materias aprobadas.")
    input("Presione una tecla para continuar...  ")


def menu(alumnos: dict, materias: dict) -> None:
    continuar_en_menu = True
    hay_alumnos = False

    while continuar_en_menu:
        limpiar_pantalla()
        
        opciones = [
            "Ingresar alumnos al sistema", 
            "Ver antigüedad promedio por carrera de los alumnos activos", 
            "Ver mejor alumno activo de la facultad", 
            "Ver promedio de materias aprobadas de una carrera", 
            "Ver departamento con la mayor cantidad de materias aprobadas",
            "Salir",
        ]
        
        for i in range(len(opciones)):
            print(f"{i + 1} - {opciones[i]}")

        opcion = ingresar_opcion(len(opciones))

        if opcion == 1:
            alta_alumnos(alumnos, materias)
            hay_alumnos = True
        elif opcion == 2:
            if not hay_alumnos:
                input("No se han ingresado aún los alumnos al sistema. Presione una tecla para continuar...  ")
            else:
                antiguedad_promedio_carrera(alumnos)
        elif opcion == 3:
            if not hay_alumnos:
                input("No se han ingresado aún los alumnos al sistema. Presione una tecla para continuar...  ")
            else:
                mejor_alumno_facultad(alumnos, materias)
        elif opcion == 4:
            if not hay_alumnos:
                input("No se han ingresado aún los alumnos al sistema. Presione una tecla para continuar...  ")
            else:
                promedio_materias_aprobadas_carrera(alumnos, materias)
        elif opcion == 5:
            if not hay_alumnos:
                input("No se han ingresado aún los alumnos al sistema. Presione una tecla para continuar...  ")
            else:
                departamento_mas_aprobados(alumnos, materias)
        elif opcion == 6:
            continuar_en_menu = False


def main() -> None:
    # datos de ejemplo

    alumnos = {
        123456: {
            "nombre": "Juan",
            "apellido": "Perez",
            "carrera": "Ingeniería en Informática",
            "anio_ingreso": 2017,
        },
    }

    materias = {
        123456: {
            "75.40": 10,
            "62.01": 7,
            "61.03": 8,
        },
    }

    menu(alumnos, materias)


main()
