'''
 Yamila, la cosmetóloga furor en redes, tiene un consultorio donde realiza limpiezas y tratamientos para el cuidado
de la piel.
Debido a la alta demanda de sus pacientes y futuros pacientes, nos pidió que realicemos un programa que la ayude
con la planificación de su negocio. La información del paciente que Yami necesita analizar es la cantidad de consultas
asistidas y que tratamientos fueron realizados.

Asimismo, el catálogo de tratamientos que comercializa es el siguiente:
- Higiene profunda $1500
- Tratamiento Acné $1500
- Tratamiento tensor con aparatología $1800
- Tratamiento revitalizante $3000

Hacer un programa que:
a) Permita al usuario realizar el ingreso de un paciente. Para ello se solicita:
- DNI
- Nombre y Apellido
- Cantidad de consultas asistidas
- Tratamientos realizados (Tipo y cantidad. Puede ser ninguno)
b) Emita un reporte que informe el tratamiento más solicitado por los pacientes.
c) Emita un reporte que informe el monto total de tratamientos vendidos.
d) Emita un reporte que informe el total de pacientes nuevos y viejos.
e) Emita un reporte que informe cuál es el tratamiento más solicitado por los pacientes nuevos.

A tener en cuenta: Se considera que un paciente es *nuevo* en caso de que el mismo haya asistido únicamente a 1
consulta con el profesional.
'''


def ingresar_opcion(rango_opciones: int) -> int:
    opcion = input(">>> Ingrese la opción:   ")
    while not (opcion.isnumeric() and 0 < int(opcion) <= rango_opciones):
        if rango_opciones == 1:
            opcion = input("Pulse 1 >>>   ")
        else:
            opcion = input(f"Ingrese una opcion entre 1 y {rango_opciones} >>>   ")

    return int(opcion)


def mostrar(listado: dict, titulo: str) -> None:
    print(titulo + ":")

    for elemento in listado:
        print(f"{elemento} - {listado[elemento]}")


def tratamiento_mas_solicitado_nuevos(pacientes: dict) -> None:
    mejores_tratamientos_nuevos = dict()

    for paciente in pacientes:
        for tratamiento in pacientes[paciente][2]:
            if pacientes[paciente][1] == 1:
                if tratamiento not in mejores_tratamientos_nuevos:
                    mejores_tratamientos_nuevos[tratamiento] = pacientes[paciente][2][tratamiento]
                else:
                    mejores_tratamientos_nuevos[tratamiento] += pacientes[paciente][2][tratamiento]

    max_iniciador = False
    maximo = list()

    for elemento in mejores_tratamientos_nuevos:
        if max_iniciador == False:
            maximo = [elemento, mejores_tratamientos_nuevos[elemento]]
            max_iniciador = False
        
        if mejores_tratamientos_nuevos[elemento] >= maximo[1]:
            maximo = [elemento, mejores_tratamientos_nuevos[elemento]]
    
    print(f"El tratamiento más solicitado por los pacientes nuevos es '{maximo[0]}' con {maximo[1]} solicitudes")


def total_pacientes_nuevos_viejos(pacientes: dict) -> None:
    pacientes_nuevos = 0; pacientes_viejos = 0

    for paciente in pacientes:
        if pacientes[paciente][1] == 1:
            pacientes_nuevos += 1
        else:
            pacientes_viejos += 1

    print(f"La cantidad de pacientes nuevos es de: {pacientes_nuevos}")
    print(f"La cantidad de pacientes viejos es de: {pacientes_viejos}")


def total_tratamientos_vendidos(tratamientos: dict, pacientes: dict) -> None:
    monto_total = 0
    
    for paciente in pacientes:
        for tratamiento in pacientes[paciente][2]:
            monto_paciente = tratamientos[tratamiento] * pacientes[paciente][2][tratamiento]
            monto_total += monto_paciente

    print(f"El monto total de tratamientos vendidos es: ${monto_total}")


def ver_tratamiento_mas_solicitado(pacientes: dict) -> None:
    # tratamientos_totales = {tratamiento: cantidad_solicitudes}
    tratamientos_totales = dict()

    for paciente in pacientes:
        for tratamiento in pacientes[paciente][2]:
            if tratamiento not in tratamientos_totales:
                tratamientos_totales[tratamiento] = pacientes[paciente][2][tratamiento]
            else:
                tratamientos_totales[tratamiento] += pacientes[paciente][2][tratamiento]

    max_iniciador = False
    maximo = list()

    for elemento in tratamientos_totales:
        if max_iniciador == False:
            maximo = [elemento, tratamientos_totales[elemento]]
            max_iniciador = False
        
        if tratamientos_totales[elemento] >= maximo[1]:
            maximo = [elemento, tratamientos_totales[elemento]]
    
    print(f"El tratamiento más solicitado es '{maximo[0]}' con {maximo[1]} solicitudes")


def ingresar_paciente(listado_tratamientos: dict, pacientes: dict) -> None:
    nuevo_paciente = list()
    tratamientos_realizados = dict()

    dni = int(input("Ingrese el DNI del paciente:  "))
    nombre_apellido = input("Ingrese el Nombre y Apellido del paciente:  ")
    cant_consultas_asist = int(input("Ingrese la cantidad de consultas a las que asisitió el paciente:  "))

    ingresar_tratamientos = True

    aux_tratamiento = input("¿El paciente se ha realizado algún tratamiento antes en esta clínica? (S/N):  ").lower()
    
    if aux_tratamiento == "s":
        while ingresar_tratamientos:
            mostrar(listado_tratamientos, "Tratamientos")
            tipo = input("Escriba el nombre del tratamiento realizado por el paciente:  ")
            cantidad = int(input("¿Cuántas veces se realizó este tratamiento?:  "))
            tratamientos_realizados[tipo] = cantidad
            if input("¿Desea seguir ingresando tratamientos del paciente? (S/N)?").lower() == "n":
                ingresar_tratamientos = False
    
    nuevo_paciente = [nombre_apellido, cant_consultas_asist, tratamientos_realizados]
    pacientes[dni] = nuevo_paciente
    print("Se agregó al paciente exitosamente.")
        

def menu(tratamientos: dict, pacientes: dict) -> None:
    continuar_en_menu = True

    while continuar_en_menu:
        print("COSMETOLOGÍA 'YAMILA'\n")
        print("1 - Ingresar un paciente")
        print("2 - Ver tratamiento más solicitado por los pacientes")
        print("3 - Ver monto total de tratamientos vendidos")
        print("4 - Ver total de pacientes nuevos y viejos")
        print("5 - Ver tratamiento más solicitado por los pacientes nuevos")
        print("6 - Salir")

        opcion = ingresar_opcion(6)

        if opcion == 1:
            ingresar_paciente(tratamientos, pacientes)
        if opcion == 2:
            ver_tratamiento_mas_solicitado(pacientes)
        if opcion == 3:
            total_tratamientos_vendidos(tratamientos, pacientes)
        if opcion == 4:
            total_pacientes_nuevos_viejos(pacientes)
        if opcion == 5:
            tratamiento_mas_solicitado_nuevos(pacientes)
        if opcion == 6:
            continuar_en_menu = False


def main() -> None:
    tratamientos = {
        # nombre_tratamiento: precio,
        "Higiene profunda": 1500,
        "Tratamiento Acné": 1500,
        "Tratamiento tensor con aparatología": 1800,
        "Tratamiento revitalizante": 3000
    }

    pacientes = {
        # DNI: [nombre_apellido, cant_consultas_asist, tratamientos_realizados = {tipo: cantidad}]
        125 : ["Juan Perez", 1, {"Tratamiento Acné": 1}],
        126 : ["María Suárez", 1, {"Tratamiento revitalizante": 2, "Higiene profunda": 3}],
        127 : ["Carla Sánchez", 2, {}]
    }
    
    menu(tratamientos, pacientes)


main()
