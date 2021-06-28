
MENU = {
    "Baguette Clásica": 250,
    "Baguette Rellena": 350,
    "Baguette Vegana": 250,
    "Baguette con Muzzarella (a la pizza)": 500,
    "Merlot": 300,
    "Vin rosé": 300,
    "Borgoña blanc": 550
}


def altaCliente(clientes, dni_cliente):

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    clientes[dni_cliente] = nombre + " " + apellido


def mostrar_opciones_pedidos():
    print("\nLista de productos")
    for producto in MENU:
        print(f"{producto}: ${MENU[producto]}")


def ingreso_pedido():
    mostrar_opciones_pedidos()

    producto_elegido = input("\nIngrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = cantidad * MENU[producto_elegido]

    return (producto_elegido, cantidad, precio)


def agregar_pedido_a_compras(dni, compras):
    pedido = ingreso_pedido()

    if dni in compras:
        compras[dni].append(pedido)
    else:
        compras[dni] = [pedido]


def realizar_pedido(clientes, compras):
    dni_ingresado = int(input("Ingrese su DNI: "))

    if dni_ingresado not in clientes:
        altaCliente(clientes, dni_ingresado)

    # dni_ingresado existe en clientes

    seguir_pidiendo = True
    while seguir_pidiendo:

        agregar_pedido_a_compras(dni_ingresado, compras)

        opcion_seguir_pidiendo = input("\nDesea agregar otro pedido? (S/N)")
        if opcion_seguir_pidiendo != "S":
            seguir_pidiendo = False


def ingresar_pago(pagos):
    """Asumo que el dni ingresado va a estar en la lista de clientes"""
    dni = int(input("Ingrese su dni: "))
    pago_actual = int(input("Ingrese el monto a pagar: "))

    if dni in pagos:
        pagos[dni].append(pago_actual)
    else:
        pagos[dni] = [pago_actual]


def actualizar_deudas(deudas, compras, pagos):

    for dni_cliente in compras:
        deuda_actual = 0

        if dni_cliente in compras:
            for pedido in compras[dni_cliente]:
                deuda_actual += pedido[2]

        if dni_cliente in pagos:
            for pago in pagos[dni_cliente]:
                deuda_actual -= pago

        deudas[dni_cliente] = deuda_actual


def ranking_deudas(clientes, deudas) -> None:
    """
    Muestra por pantalla el ranking de mayores deudoras hasta un maximo de 5.

    :param clientes: diccionario que contiene los clientes del sistema
    :param deudas: diccionario que contiene las deudas
    :return: None
    """
    lista_deudas = [] # [ [DEUDA, NOMBRE+APELLIDO] ]
    for dni_cliente in deudas:
        lista_deudas.append([deudas[dni_cliente], clientes[dni_cliente]])

    lista_deudas.sort(reverse=True)


    print("\nEl ranking de deudores es")

    cantidad_maxima = 5 if (len(lista_deudas) > 5) else len(lista_deudas)

    for i in range(cantidad_maxima):
        print(f"{lista_deudas[i][1]} : ${lista_deudas[i][0]}")


def reporte_pedidos(pedidos):
    dict_products = {}

    for dni_cliente in pedidos:
        for pedido in pedidos[dni_cliente]:
            nombre_producto = pedido[0]
            if nombre_producto in dict_products:
                dict_products[nombre_producto] += 1
            else:
                dict_products[nombre_producto] = 1

    for producto in dict_products:
        print(f"{producto} - {dict_products[producto]}")


def pedidos_superiores_a(pedidos, monto = 1000):

    pedidos_totales = 0
    pedidos_superiores = 0

    for dni_cliente in pedidos:
        pedidos_totales += len(pedidos[dni_cliente])
        for pedido in pedidos[dni_cliente]:
            if (pedido[2] > monto):
                pedidos_superiores += 1

    if pedidos_totales > 0:
        print(f"El porcentaje de pedidos superiores a: ${monto} es %{pedidos_superiores*100/pedidos_totales}")
    else:
        print("No hay pedidos registrados")


def mostrar_menu():
    print("Opciones")
    print("1- Realizar pedido")
    print("2- Ingresar un pago")
    print("3- Top 5 de deudas")
    print("4- Reporte de pedidos")
    print("5- Pedidos superiores a un monto")


def main():

    clientes = {} #key = DNI : value = NOMBRE + APELLIDO
    compras = {} #key = DNI : value = LISTA DE PEDIDOS
    pagos = {} #key = DNI : value = LISTA DE PAGOS
    deudas = {} #key = DNI : value = LISTA DE DEUDAS

    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("\nIngrese una opcion: ")

        if opcion == "1":
            realizar_pedido(clientes, compras)
            actualizar_deudas(deudas,compras, pagos)

        elif opcion == "2":
            ingresar_pago(pagos)
            actualizar_deudas(deudas, compras, pagos)

        elif opcion == "3":
            ranking_deudas(clientes, deudas)

        elif opcion == "4":
            reporte_pedidos(compras)

        elif opcion == "5":
            pedidos_superiores_a(compras, monto=4000)

        opcion_continuar = input("Desea realizar otra operacion? (S/N)")
        if opcion_continuar != "S":
            continuar = False


main()
