'''
Ejercicio) 

“@RumboCircular” es un emprendimiento que enseña a cuidar el medioambiente. Rumbo Circular 
además de dictar cursos de capacitación sobre medioambiente en empresas, 
lanzó un conjunto de cursos para la comunidad general.

Estos cursos son los siguientes:

    - Aprendé a hacer tu propio compost (1 día de curso). Costo $950
    - Los niños y el medioambiente (para padres e hijos) (2 días de curso). Costo $990
    - Tu huerta orgánica (4 días de curso). Costo $2500


El gran éxito de de estos cursos hizo que RumboCircular nos consultara para que los asesoremos 
para la creación de un pequeño sistema que permita organizar la asistencia de los participantes.

Los requerimientos que nos solicitan son los siguientes:

    a - ABM (Alta – Baja – Modificación) de cursos. Se podrá cargar la siguiente infomación de los cursos. 
        Nombre, cantidad de días (duración), costo, cantidad de vacantes, fechas de dictado.
    b - Listar todos los cursos cuyo costo sea superior a 1150 pesos.
    c - Mostrar el o los cursos cuya cantidad de vacantes se la máxima.
    d - Mostrar todos los cursos que tengan al menos 3 fechas de dictado.
'''
import os


def limpiar_pantalla() -> None:
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def ingresar_opcion(rango_opciones: int) -> int:
    '''
    PRE: El rango de opciones tiene que ser un número entero
    POST: Devuelve una opción representada por un número entero dentro del rango
    '''
    opcion = input(">>> Ingrese la opción:   ")
    while not (opcion.isnumeric() and 0 < int(opcion) <= rango_opciones):
        if rango_opciones == 1:
            opcion = input("Pulse 1 >>>   ")
        else:
            opcion = input(f"Ingrese una opcion entre 1 y {rango_opciones} >>>   ")
    return int(opcion)


def salir() -> None:
    input("PRESIONE ENTER PARA SALIR ")


def chocolate() -> None:
    limpiar_pantalla()
    print("BASE DE DATOS DE 'RUMBO CIRCULAR'\n")
    print("---------------------------------\n")


def listar_cursos_costo(cursos: dict, costo_superior_a: int) -> list:
    chocolate()

    cursos_costo = list()
    print(f"Los cursos con costo superior a 1150 son: {cursos_costo}\n\n")

    salir()


def listar_cursos_llenos(cursos: dict) -> list:
    chocolate()

    cursos_llenos = list()
    print(f"Los cursos llenos son: {cursos_llenos}\n\n")

    salir()


def listar_cursos_fechas(cursos: dict, min_fechas: int) -> list:
    chocolate()

    cursos_fechas = list()
    print(f"Los cursos con al menos 3 fechas de dictado son: {cursos_fechas}\n\n")

    salir()


def alta_cursos(cursos: dict) -> None:
    chocolate()

    curso = dict()
    seguir_ingresando_fechas = True
    
    print("DAR DE ALTA UN CURSO")
    llave = input("Ingrese codigo curso >>>   ")
    nombre = input("Ingrese nombre curso >>>   ")
    costo = input("Ingrese costo curso >>>   ")
    dias = input("Ingrese cantidad dias curso >>>   ")
    vacantes = input("Ingrese cantidad vacantes curso >>>   ")
    fechas_de_dictado = list()

    while seguir_ingresando_fechas:
        fecha = input(f"Ingrese las fechas del curso")
        fechas_de_dictado.append(fecha)
        print("Presione 1 para seguir ingresando fechas, 2 para salir >>>  ")
        salir = ingresar_opcion(2)
        if salir == 2:
            seguir_ingresando_fechas = False

    curso["nombre"] = nombre
    curso["costo"] = costo
    curso["cantidad_de_dias"] = dias
    curso["cantidad_de_vacantes"] = vacantes
    curso["fechas_de_dictado"] = fechas_de_dictado

    cursos[llave] = curso
   

def baja_cursos(cursos: dict) -> None:
    chocolate()

    opcion = 0

    print("DAR DE BAJA UN CURSO")

    for key, value in cursos.items():
        llave = "nombre"
        print(f"{key} - {value[llave]}")

    print("¿Cual curso desea BORRAR?")
    opcion = ingresar_opcion(len(cursos))

    cursos.pop(opcion)


def modificacion_cursos(cursos: dict) -> None:
    chocolate()

    opcion = 0

    print("DAR DE BAJA UN CURSO")

    for key, value in cursos.items():
        llave = "nombre"
        print(f"{key} - {value[llave]}")

    print("¿Cual curso desea modificar?")
    opcion = ingresar_opcion(len(cursos))

    for key, value in cursos[opcion].items():
        print(f"{key} - {value}")

    entrada = input("¿Qué desea modificar del curso? >>>   ")

    if entrada == "nombre":
        nombre = input(f"Ingrese el nuevo {entrada}")
        cursos[opcion][entrada] = nombre
    elif entrada == "costo":
        costo = float(input(f"Ingrese el nuevo {entrada}"))
        cursos[opcion][entrada] = costo
    elif entrada == "cantidad_de_dias":
        cantidad_de_dias = int(input(f"Ingrese el nuevo {entrada}"))
        cursos[opcion][entrada] = cantidad_de_dias
    elif entrada == "cantidad_de_vacantes":
        cantidad_de_vacantes = int(input(f"Ingrese el nuevo {entrada}"))
        cursos[opcion][entrada] = cantidad_de_vacantes
    elif entrada == "fechas_de_dictado":
        fechas_de_dictado = list()
        seguir_ingresando_fechas = True
        
        while seguir_ingresando_fechas:
            fecha = input(f"Ingrese las nuevas {entrada}")
            fechas_de_dictado.append(fecha)
            print("Presione 1 para seguir ingresando fechas, 2 para salir >>>  ")
            salir = ingresar_opcion(2)
            if salir == 2:
                seguir_ingresando_fechas = False


def abm_cursos(cursos: dict) -> None:
    chocolate()

    print("ABM")
    print("1) Alta de datos")
    print("2) Baja de datos")
    print("3) Modificación de datos")
    print("4) Atrás")
    opcion = ingresar_opcion(3)

    if opcion == 1:
        alta_cursos(cursos)
    elif opcion == 2:
        baja_cursos(cursos)
    elif opcion == 3:
        modificacion_cursos(cursos)


def main() -> None:
    cursos = {
        1: {
            "nombre": "aprende a hacer tu propio compost",
            "costo": 950.0,
            "cantidad_de_dias": 1,
            "cantidad_de_vacantes": 4,
            "fechas_de_dictado": ["10/06/2021"]
        },

        2: {
            "nombre": "los niños y el medioambiente",
            "costo": 990.0,
            "cantidad_de_dias": 2,
            "cantidad_de_vacantes": 5,
            "fechas_de_dictado": ["09/06/2021", "15/06/2021"]
        },

        3: {
            "nombre": "Tu huerta orgánica",
            "costo": 2500.0,
            "cantidad_de_dias": 4,
            "cantidad_de_vacantes": 4,
            "fechas_de_dictado": ["10/06/2021", "14/06/2021", "17/06/2021"]
        }
    }

    salir = False

    while salir == False:
        chocolate()
        print('1) - ABM (Alta – Baja – Modificación) de cursos.')
        print('2) - Listar todos los cursos cuyo costo sea superior a 1150 pesos.')
        print('3) - Mostrar el o los cursos cuya cantidad de vacantes se la máxima.')
        print('4) - Mostrar todos los cursos que tengan al menos 3 fechas de dictado.')
        print("5) - Salir")
        opcion = ingresar_opcion(5)

        if opcion == 1:
            abm_cursos(cursos)
        elif opcion == 2:
            listar_cursos_costo(cursos, 1150)
        elif opcion == 3:
            listar_cursos_llenos(cursos)
        elif opcion == 4:
            listar_cursos_fechas(cursos, 3)
        else:
            salir = True
    
    chocolate()
    print("Nos vemos la próxima\n\n")


main()


# cursos = {
#   codigo: {
#       nombre: str
#       costo: float
#       cantidad_de_dias: int
#       cantidad_de_vacantes: int
#       fechas_de_dictado: list(str(dd/mm/yy))
#   }
# }

# cursos.get("nombre")  //  cursos["nombre"]