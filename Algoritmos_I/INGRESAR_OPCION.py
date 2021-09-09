
def ingresar_opcion(rango_opciones: int) -> int:

    opcion = input(">>> Ingrese la opción:   ")
    
    while not (opcion.isnumeric() and 0 < int(opcion) <= rango_opciones):
        if rango_opciones == 1:
            opcion = input("Pulse 1 >>>   ")
        else:
            opcion = input(f"Ingrese una opcion entre 1 y {rango_opciones} >>>   ")

    return int(opcion)


def main() -> None:
    opciones = ["Ejecutar acción uno", "Ejecutar acción dos", "Ejecutar acción tres", "Ejecutar acción cuatro"]
    for i in range(len(opciones)): print(f"{i + 1}) {opciones[i]}")
    opcion = ingresar_opcion(len(opciones))
    print(f"Usted ha elegido la opción: {opcion}")


main()
