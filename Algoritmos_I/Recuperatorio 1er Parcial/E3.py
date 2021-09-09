# RECUPERATORIO DEL 1ER PARCIAL DE ALGORTIMOS Y PROGRAMACIÓN I
# ALUMNO: PALAVECINO ARNOLD, NESTOR FABIAN
# ---------------------------------------------------------------------------------------------------------------------

# EJERCICIO 3


def ingresar_opcion(rango_opciones: int) -> int:
    opcion = input(">>> Ingrese la opción:   ")
    while not (opcion.isnumeric() and 0 < int(opcion) <= rango_opciones):
        if rango_opciones == 1:
            opcion = input("Pulse 1 >>>   ")
        else:
            opcion = input(f"Ingrese una opcion entre 1 y {rango_opciones} >>>   ")

    return int(opcion)


def pronostico_quiebre_stock(caja: dict, productos: dict) -> None:
    estimado_mensual = 30/len(caja)

    # productos_general = {producto: veces_compradas}
    productos_general = dict()

    # productos_proyeccion_mensual = {producto: veces_compradas * estimado_mensual}
    productos_proyeccion_mensual = dict()

    for dia in caja:
        for producto in caja[dia]:
            if producto not in productos_general:
                productos_general[producto] = caja[dia][producto]
            else:
                productos_general[producto] += caja[dia][producto]
    
    for elemento in productos_general:
        productos_proyeccion_mensual[elemento] = productos_general[elemento] * estimado_mensual

    print("En 30 dias se le va a acabar el stock de: ")
    for elemento in productos_proyeccion_mensual:
        if productos_proyeccion_mensual[elemento] > productos[elemento][0]:
            print(elemento)


def ordenar_productos_ascendente(frigo_produ_sin_ordenar: list) -> None:
    lista_aux = list(frigo_produ_sin_ordenar)
        
    for num_pasada in range(len(lista_aux)-1,0,-1):
        for i in range(num_pasada):
            if lista_aux[i][1] > lista_aux[i+1][1]:
                temp = lista_aux[i]
                lista_aux[i] = lista_aux[i+1]
                lista_aux[i+1] = temp

    return lista_aux   


def reporte_stock_frigorifico(productos: dict) -> None:
    # frigo_produ = {frigorifico: [productos]}
    frigo_produ = dict()
    
    for elemento in productos:
        producto, frigorifico = elemento.split("/")

        if frigorifico not in frigo_produ:
            frigo_produ[frigorifico] = [producto]
        else:
            frigo_produ[frigorifico].append(producto)
    
    for elemento in frigo_produ:
        print(f"{elemento}")
    
    opcion = input("Ingrese el frigorifico que desea ver: ")

    # frigo_produ_sin_ordenar = [[producto, precio], [producto, precio]]
    frigo_produ_sin_ordenar = list()

    for prod in frigo_produ[opcion]:
        nombre_producto = prod + "/" + opcion
        frigo_produ_sin_ordenar.append([ nombre_producto, productos[nombre_producto][1] ])

    # frigo_produ_ordenado = [[producto, precio], [producto, precio]]
    frigo_produ_ordenado = ordenar_productos_ascendente(frigo_produ_sin_ordenar)

    print(opcion.upper())
    for elemento in frigo_produ_ordenado:
        print(f"{elemento[0]} - ${elemento[1]}/100 G.")


def ordenar_descendente_comprados(lista_compras) -> list:
    lista_aux = list()

    for elemento in lista_compras:
        lista_aux.append([elemento, lista_compras[elemento]])
        
    for num_pasada in range(len(lista_aux) - 1, 0, -1):
        for i in range(num_pasada):
            if lista_aux[i][1] < lista_aux[i+1][1]:
                temp = lista_aux[i]
                lista_aux[i] = lista_aux[i+1]
                lista_aux[i+1] = temp

    return lista_aux


def reporte_producto_mas_comprado(caja: dict, compras_del_dia: dict) -> None:
    # lista_compras = {producto: cantidad}
    lista_compras = dict()

    for dia in caja:
        for producto in caja[dia]:
            if producto not in lista_compras:
                lista_compras[producto] = caja[dia][producto]
            else:
                lista_compras[producto] += caja[dia][producto]
    
    for producto in compras_del_dia:
        if producto not in lista_compras:
            lista_compras[producto] = compras_del_dia[producto]
        else:
            lista_compras[producto] += compras_del_dia[producto]
    
    lista_compras_ordenada  = ordenar_descendente_comprados(lista_compras)

    for i in range(len(lista_compras_ordenada)):
        print(f"{lista_compras_ordenada[i][0]} - {lista_compras_ordenada[i][1]}")


def nueva_compra(productos: dict, compras_del_dia: dict, monto_total_dia: list) -> None:
    seguir_pidiendo = True
    pedido = dict()
    monto_total = 0

    for elemento in productos:
        print(f"{elemento} - Stock: {productos[elemento][0]} Kg. - precio por 100g: {productos[elemento][1]}")

    while seguir_pidiendo:
        producto_pedido = input("Seleccione el producto que desea: ")
        cantidad_pedida = input("¿Cuántos gramos desea?:  ")

        cantidad_pedida_kilos = int(cantidad_pedida) / 1000

        if productos[producto_pedido][0] < cantidad_pedida_kilos:
            print(f"Disculpe, no tenemos esa cantidad de gramos de {producto_pedido}")
            print(f"Nos quedan {productos[producto_pedido][0] * 10} gramos disponibles")
        else:
            pedido[producto_pedido] = cantidad_pedida_kilos
            monto_total += productos[producto_pedido][1] * 10 * cantidad_pedida_kilos

            if input("¿Desea pedir otra cosa (S/N)?: ").lower() == "n":
                seguir_pidiendo = False

    print(f"El monto total a pagar es: {monto_total}")
    input("Ingrese ENTER cuando el usuario pague (solo efectivo):  ")
    monto_total_dia[0] += monto_total

    for producto in pedido:
        compras_del_dia[producto] = pedido[producto]


def menu(productos: dict, caja: dict, contador_dias: list, compras_del_dia: dict, monto_total_dia: list) -> None:
    continuar_en_menu = True
    caja_abierta = False

    while continuar_en_menu:
        print("FIAMBRERIA 'LOS SABORES DE ARI'")
        print("1 - Apertura de Caja")
        print("2 - Nueva Compra")
        print("3 - Reporte producto mas comprado")
        print("4 - Reporte stock por frigorifico")
        print("5 - Cierre de caja")
        print("6 - Pronóstico de quiebre de stock")
        print("7 - Salir")
        opcion = ingresar_opcion(7)

        if opcion == 1:
            if input("¿Seguro que desea cerrar la caja? (S/N)").lower() == "s":
                caja_abierta = True
                contador_dias[0] += 1
                caja[contador_dias[0]] = dict()
                print("Usted ha abierto la caja")
            else:
                print("Usted decidió no abrir la caja.")
        if opcion == 2:
            if caja_abierta:
                nueva_compra(productos, compras_del_dia, monto_total_dia)
            else:
                print("No puede realizar una nueva compra hasta que ABRA la caja")
        if opcion == 3:
            reporte_producto_mas_comprado(caja, compras_del_dia)
        if opcion == 4:
            reporte_stock_frigorifico(productos)
        if opcion == 5:
            if not caja_abierta:
                print("La caja ya está cerrada. No puede cerrarla.")
            else:
                if input("¿Seguro que desea cerrar la caja? (S/N)").lower() == "s":
                    caja_abierta = False
                    caja[contador_dias[0]] = compras_del_dia
                    compras_del_dia.clear()
                    print("Usted ha cerrado la caja.")
                else:
                    print("Usted ha decidido no cerrar la caja.")
        if opcion == 6:
            pronostico_quiebre_stock(caja, productos)
        if opcion == 7:
            continuar_en_menu = False


def main() -> None:
    productos = {
        "Jamón Cocido/Bocatti": [20, 189],
        "Jamón Cocido/Rogiano": [10, 117],
        "Jamón Cocido/Paladini": [5, 113],
        "Jamón Cocido/Tapalque": [12,79],
        "Salame milán/La piamontesa": [7, 118],
        "Salame milán/Bocatti": [3, 157],
        "Salame milán/Paladini": [4, 121],
        "Mortadela/Calchaqui": [11, 82],
        "Mprtadela/Paladini": [5, 90],
        "Mortadela/Trozer": [3, 49],
    }

    caja = {
        # dia: {producto: veces_compradas}
        19: {
            "Jamón Cocido/Bocatti": 2, 
            "Salame milán/La piamontesa": 3
            }
    }

    contador_dias = [0,]

    # compras_del_dia = {producto: cantidad}
    compras_del_dia = dict()

    monto_total_dia = [0,]

    menu(productos, caja, contador_dias, compras_del_dia, monto_total_dia)


main()
