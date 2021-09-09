'''
1° PARCIAL DE ALGORITMOS Y PROGRAMACIÓN I

PALAVECINO ARNOLD, NESTOR FABIAN
'''

# EJERCICIO 3


import os


def limpiar_pantalla() -> None:
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def ingresar_opcion_int(rango_opciones: int) -> int:
    opcion = input(">>> Ingrese la opción:   ")
    while not (opcion.isnumeric() and 0 < int(opcion) <= rango_opciones):
        if rango_opciones == 1:
            opcion = input("Pulse 1 >>>   ")
        else:
            opcion = input(f"Ingrese una opcion entre 1 y {rango_opciones} >>>   ")
    return int(opcion)


def salir() -> None:
    input("PRESIONE ENTER PARA SALIR ")


def ingresar_pedidos(clientes: dict, pedidos: dict, menu_panaderia: dict) -> None:
    dni = input("Ingrese su DNI >>>  ")
    monto = 0

    if dni not in clientes:
        nombre = input("Ingrese su nombre >>> ")
        clientes[dni] = nombre

    for i in range(len(menu_panaderia)):
        print(f"{menu_panaderia[i+1].items()}")

    pedidos_aux = list()

    id_pedido = int(input("ingrese id pedido >>> "))

    while pedido != -1:
        pedido = int(input("Ingrese el producto que desea pedir o -1 para salir >>> "))
        pedidos_aux.append(pedido)
        monto += menu_panaderia[pedido]["monto_total"]

    nuevo_pedido = dict()

    nuevo_pedido["dni_cliente"] = dni
    nuevo_pedido["articulos"] = pedidos_aux
    nuevo_pedido["monto_total"] = monto
    nuevo_pedido["pagado"] = 0
    
    pedidos[id_pedido] = nuevo_pedido

    salir()


def ingresar_pagos(pedidos: dict) -> None:
    dni = int(input("Ingrese su DNI >>>  "))
    print("Sus pedidos son: ")

    for i in range(len(pedidos)):
        if pedidos[i+1]["dni_cliente"] == dni:
            print(f"{pedidos[i+1].items()}")
        
    pedido_pagar = int(input("Seleccione el pedido a pagar >>>  "))
    monto_pagar = int(input("Seleccione el monto a pagar >>>  "))

    pedidos[pedido_pagar]["monto_total"] -= monto_pagar

    print(f"Usted ha pagado {monto_pagar}")

    salir()


def ver_top_5_deudas(clientes: dict, pedidos: dict) -> None:
    pass

def imprimir_reporte_articulos(clientes: dict, pedidos: dict, menu_panaderia: dict) -> None:
    pass

def porcentaje_pedidos_sup_1000(clientes: dict, pedidos: dict, menu_panaderia: dict) -> None:
    pass


def menu(clientes: dict, pedidos: dict, menu_panaderia: dict, salir: bool) -> bool:
    print('1) - Ingresar pedidos')
    print('2) - Ingresar pagos')
    print('3) - Ver Top 5 deudas más importantes')
    print('4) - Imprimir reporte de artículos en pedidos')
    print('5) - Indicar el porcentaje de pedidos superiores a $1000')
    print("6) - Salir\n")
    opcion = ingresar_opcion_int(6)

    if opcion == 1:
        ingresar_pedidos(clientes, pedidos, menu_panaderia)
    elif opcion == 2:
        ingresar_pagos(pedidos)
    elif opcion == 3:
        ver_top_5_deudas(clientes, pedidos)
    elif opcion == 4:
        imprimir_reporte_articulos(clientes, pedidos, menu_panaderia)
    elif opcion == 5:
        porcentaje_pedidos_sup_1000(clientes, pedidos, menu_panaderia)
    else:
        salir = True

    return salir


def main() -> None:
    clientes = {
        41234567: {
            "nombre": "Pepito Juarez",
        },
        46221233: {
            "nombre": "Mariana Sanchez",
        },
    }

    pedidos = {
        1: {
            "dni_cliente": 41234567,
            "articulos" : [4,4,4,4,4],
            "monto_total": 2500,
            "pagado": 1350
        },
        2: {
            "dni_cliente": 46221233,
            "articulos" : [5,5,5],
            "monto_total": 1200,
            "pagado": 1200
        }
    }

    menu_panaderia = {
        1: {
            "nombre": "Baguette Clásica",
            "precio": 250
        },
        2: {
            "nombre": "Baguette Rellena",
            "precio": 350
        },
        3: {
            "nombre": "Baguette Vegana",
            "precio": 250
        },
        4: {
            "nombre": "Baguette con Muzzarella (a la pizza)",
            "precio": 500
        },
        5: {
            "nombre": "Merlot",
            "precio": 300
        },
        6: {
            "nombre": "Vin rosé",
            "precio": 300
        },
        7: {
            "nombre": "Borgoña blanc",
            "precio": 550
        },
    }

    elementos = clientes
    salir = False

    while salir == False:
        salir = menu(clientes, pedidos, menu_panaderia, salir)
    

    print("Nos vemos la próxima\n\n")


main()
