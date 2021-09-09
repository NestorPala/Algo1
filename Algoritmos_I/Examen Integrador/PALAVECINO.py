#INTEGRADOR DE ALGORITMOS Y PROGRAMACIÓN I
#2021-08-17
#PALAVECINO ARNOLD, NESTOR FABIAN


import os
from pathlib import Path


RUTA_STOCK_TXT = f"{Path.home()}\\Desktop\\stock.txt"
RUTA_OCHENTA_TXT = f"{Path.home()}\\Desktop\\ochenta.txt"


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


def procesar_archivo(stock: dict) -> None:
    with open(RUTA_STOCK_TXT, mode = 'r', encoding = "utf-8") as archivo_txt:
        next(archivo_txt)

        for fila in archivo_txt:
            campos = fila.split(";")
            campos[len(campos) - 1] = campos[len(campos) - 1].rstrip("\n")

            codigo_interno = int(campos[0])
            nuevo_producto = dict()

            nuevo_producto["codigo_interno"] = int(campos[1])
            nuevo_producto["equipo"] = campos[2]
            nuevo_producto["tipo"] = campos[3]
            nuevo_producto["año"] = int(campos[4])
            nuevo_producto["marca"] = campos[5]
            nuevo_producto["talle"] = campos[6]
            nuevo_producto["ingresadas"] = int(campos[7])
            nuevo_producto["vendidas"] = int(campos[8])
            nuevo_producto["costo_promedio"] = float(campos[9])
            nuevo_producto["precio_venta_actual"] = float(campos[10])

            stock[codigo_interno] = nuevo_producto
    
    input("Se ingresaron al sistema todos los datos correctamente")


def mostrar_equipos_mayor_stock(stock: dict) -> None:
    
    equipo_cantidad = dict()

    for sku in stock:
        equipo = stock[sku]["equipo"]
        if equipo not in equipo_cantidad:
            equipo_cantidad[equipo] = (stock[sku]["ingresadas"] - stock[sku]["vendidas"])
        else:
            equipo_cantidad[equipo] += (stock[sku]["ingresadas"] - stock[sku]["vendidas"])
    
    equipo_aux = list()

    for elemento in equipo_cantidad:
        equipo_aux.append([elemento, equipo_cantidad[elemento]])
    
    equipo_aux.sort(key=lambda x: x[1], reverse=True)
    
    print("Los equipos que poseen más cantidad de remeras en stock son:")
    for i in range(3):
        print(f"{equipo_aux[i][0]} - {equipo_aux[i][1]}")

    input("Ingrese una tecla para continuar...  ")


def distribucion_porcentual_talles(stock: dict) -> None:
    cantidad_remeras_totales_vendidas = 0
    talle_cantidad = dict()

    for sku in stock:
        cantidad_remeras_totales_vendidas += stock[sku]["vendidas"]
        cantidad_remeras_vendidas = stock[sku]["vendidas"]
        talle = stock[sku]["talle"] 

        if talle not in talle_cantidad:
            talle_cantidad[talle] = cantidad_remeras_vendidas
        else:
            talle_cantidad[talle] += cantidad_remeras_vendidas
    
    talle_aux = list()
    
    for elemento in talle_cantidad:
        talle_aux.append([elemento, talle_cantidad[elemento]])

    talle_aux.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(talle_aux)):
        talle_aux[i][1] = talle_aux[i][1] / cantidad_remeras_totales_vendidas * 100
    
    print("Talles ordenados por porcentaje de ventas")

    for i in range(len(talle_aux)):
        print(f"{talle_aux[i][0]} - {talle_aux[i][1]}%")

    input("Presione una tecla para continuar...   ")


def antiguedad_promedio_ponderada_stock(stock: dict) -> None:
    stock_total_camisetas = 0

    for sku in stock:
        stock_total_camisetas += (stock[sku]["ingresadas"] - stock[sku]["vendidas"])

    antiguedad_cantidad = dict()

    for sku in stock:
        if stock[sku]["vendidas"] > 0:
            antiguedad = 2021 - stock[sku]["año"]
            if antiguedad not in antiguedad_cantidad:
                antiguedad_cantidad[antiguedad] = (stock[sku]["ingresadas"] - stock[sku]["vendidas"])
            else:
                antiguedad_cantidad[antiguedad] += (stock[sku]["ingresadas"] - stock[sku]["vendidas"])

    ponderado_aux = 0

    for elemento in antiguedad_cantidad:
        ponderado_aux += elemento * antiguedad_cantidad[elemento]
    
    ponderado = ponderado_aux / stock_total_camisetas

    print(f"La antiguedad promedio de las camisetas en stock actualmente es de {ponderado} años.")
    input("Presione una tecla para continuar...   ")
    

def ochenta_stock_valorizado(stock: dict) -> None:
    stock_valorizado = 0

    for sku in stock:
        stock_valorizado += stock[sku]["costo_promedio"] * (stock[sku]["ingresadas"] - stock[sku]["vendidas"])

    peso_relativo_costo = dict()
    
    for sku in stock:
        costo_sku = stock[sku]["costo_promedio"] * (stock[sku]["ingresadas"] - stock[sku]["vendidas"])
        peso_relativo_costo[sku] = costo_sku / stock_valorizado * 100

    costo_aux = list()
    
    for elemento in peso_relativo_costo:
        costo_aux.append([elemento, peso_relativo_costo[elemento]])
    
    costo_aux.sort(key=lambda x: x[1], reverse=True)

    ochenta = list()
    suma_pesos_relativos = 0
    i = -1

    while suma_pesos_relativos <= 80:
        i += 1
        print(i)
        suma_pesos_relativos += costo_aux[i][1]
        ochenta.append(costo_aux[i][0])
    
    print(ochenta)
    #QUEDA PENDIENTE ESCRIBIR ARCHIVO
    
    input("Presione una tecla para continuar...   ")


def menu(stock: dict) -> None:
    continuar_en_menu = True
    datos_ingresados = False

    while continuar_en_menu:
        limpiar_pantalla()
        
        opciones = [
            "Procesar archivo",
            "Mostrar por pantalla los 3 Equipos de los cuales se tienen mayor cantidad de unidades en stock, ordenados por cantidad de camisetas distintas en orden descendente",
            "Mostrar por pantalla la distribución porcentual de ventas respecto a talles ordenado descendentemente por porcentaje",
            "Mostrar por pantalla la antigüedad promedio ponderada del stock actual",
            "Determinar que artículos conforman al menos el 80 por ciento del stock valorizado",
            "Salir",
        ]
        
        for i in range(len(opciones)):
            print(f"{i + 1} - {opciones[i]}")

        opcion = ingresar_opcion(len(opciones))

        if opcion == 1:
            procesar_archivo(stock)
            datos_ingresados = True
        elif opcion == 2:
            if not datos_ingresados:
                input("Ingrese primero los datos. Presione una tecla para continuar... ")
            else:
                mostrar_equipos_mayor_stock(stock)
        elif opcion == 3:
            if not datos_ingresados:
                input("Ingrese primero los datos. Presione una tecla para continuar... ")
            else:
                distribucion_porcentual_talles(stock)
        elif opcion == 4:
            if not datos_ingresados:
                input("Ingrese primero los datos. Presione una tecla para continuar... ")
            else:
                antiguedad_promedio_ponderada_stock(stock)
        elif opcion == 5:
            if not datos_ingresados:
                input("Ingrese primero los datos. Presione una tecla para continuar... ")
            else:
                ochenta_stock_valorizado(stock)
        elif opcion == 6:
            continuar_en_menu = False


def main() -> None:
    """dato de ejemplo
        4059322286834: {
            "codigo_interno": 1,
            "equipo": "Argentina",
            "tipo": "Local",
            "año": 2018,
            "marca": "Adidas",
            "talle": "L",
            "ingresadas": 4,
            "vendidas": 1,
            "costo_promedio": 7.61,
            "precio_venta_actual": 39,
        },
    """
    stock = dict()
    menu(stock)


main()
