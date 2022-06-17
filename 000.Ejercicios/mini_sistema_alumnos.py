import os


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


def agregar_alumno(lista_alumnos: list) -> None:
    nombre = input("Ingrese el nombre del alumno >>>   ")
    padron = input("Ingrese el padrón del alumno >>>   ")
    nota = input("Ingrese la nota del alumno >>>   ")
    lista_alumnos.append([nombre,int(padron),int(nota)])


def consultar_aprobados(lista_alumnos: list) -> None:
    print("Alumnos aprobados:\n\n")

    for i in range(len(lista_alumnos)):
        if lista_alumnos[i][2] >= 4:
            print(lista_alumnos[i])

    input("Presione cualquier tecla para salir")


def mostrar_cantidad_alumnos_y_promedio(lista_alumnos: list) -> None:
    acumulador = 0

    if len(lista_alumnos) == 0:
        print("Hay 0 alumnos inscriptos en el sistema")
    else:
        print(f"Hay {len(lista_alumnos)} inscriptos en el sistema")

    for i in range(len(lista_alumnos)):
        acumulador += lista_alumnos[i][2]
    
    if len(lista_alumnos) != 0:
        print(f"La nota promedio es {acumulador/len(lista_alumnos)}")

    input("Presione cualquier tecla para salir")


def quitar_alumno(lista_alumnos: list) -> None:
    candidato = int(input("Ingrese el alumno que desea remover (por padrón)"))
    for i in range(len(lista_alumnos)):
        if lista_alumnos[i][1] == candidato:
            lista_alumnos.pop(i)


def main() -> None:
    lista_alumnos = [["Juan", 1, 8],["Pepe", 2, 3]]
    menu = True
    while menu:
        limpiar_pantalla()
        print('''Bienvenido al Sistema de Alumnos

        1 - Agregar un alumno: debe solicitarse nombre, padrón y nota.
        2 - Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.
        3 - Cantidad de alumnos totales y promedio general.
        4 - Quitar a un  alumno.
        5 - Salir
        ''')
        opcion = ingresar_opcion(5)
        if opcion == 1:
            agregar_alumno(lista_alumnos)
        elif opcion == 2:
            consultar_aprobados(lista_alumnos)
        elif opcion == 3:
            mostrar_cantidad_alumnos_y_promedio(lista_alumnos)
        elif opcion == 4:
            quitar_alumno(lista_alumnos)
        else:
            menu = False
            print("¡Adios!")
            

main()
