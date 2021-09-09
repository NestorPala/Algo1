import random


# MOSTRAR LISTA DESDE UN DICCIONARIO SIMPLE
MENU = {
    "Baguette Clásica": 250,
    "Baguette Rellena": 350,
    "Baguette Vegana": 250,
    "Baguette con Muzzarella (a la pizza)": 500,
    "Merlot": 300,
    "Vin rosé": 300,
    "Borgoña blanc": 550
}

def imprimir_diccionario_simple(diccionario: dict, forma: int) -> None:
    # Usamos un bucle simple

    if forma == 1:
        for producto in MENU:
            print(f"{producto}: ${MENU[producto]}")
    elif forma == 2:
        for clave, valor in diccionario.items():
            print(f"{clave}: ${valor}")


# imprimir_diccionario_simple(MENU, 1)


'''-------------------------------------------------------------------'''

# MOSTRAR LISTA DESDE UN DICCIONARIO COMPUESTO


PEDIDOS = {
    "1": {
        "dni_cliente": 41234567,
        "articulos" : [4,4,4,4,4],
        "monto_total": 2500,
        "pagado": 1350
    },
    "2": {
        "dni_cliente": 46221233,
        "articulos" : [5,5,5],
        "monto_total": 1200,
        "pagado": 1200
    }
}


def imprimir_diccionario_compuesto(PEDIDOS: dict, forma: int = 1) -> None:
    # Usamos un bucle anidado
    if forma == 1:
        # Sintaxis similar a listas de listas
        for id_pedido in PEDIDOS:
            print(f"PEDIDO N°{id_pedido}")
            for clave in PEDIDOS[id_pedido]:
                print(f"{clave}: {PEDIDOS[id_pedido][clave]}")
            print("\n")
    elif forma == 2:
        # Iterar con 2 variables, una para la clave y otra para el valor asociado
        for id_pedido in PEDIDOS:
            print(f"PEDIDO N°{id_pedido}")
            for clave, valor in PEDIDOS[id_pedido].items():
                print(f"{clave}: {valor}")
            print("\n")
    elif forma == 3:
        # Descomponemos dict.items() en una lista
        for id_pedido in PEDIDOS:
            lista_pedidos = list(PEDIDOS[id_pedido].items())
            print(f"PEDIDO N°{id_pedido}")
            for j in range(len(lista_pedidos)):
                print(f"{lista_pedidos[j][0]}: {lista_pedidos[j][1]}")
            print("\n")
    

def imprimir_diccionario_compuesto_tabla(PEDIDOS: dict, nombre_tabla: str) -> None:
    #Todas las claves de PEDIDOS tienen un diccionario id_pedido con las mismas claves
    lista_claves = list(PEDIDOS[random.choice(list(PEDIDOS.keys()))].keys())
    print(f"LISTA DE {nombre_tabla.upper()}\n\n")

    for i in range(len(lista_claves)):
        if i == 0: print("ID" + 18 * " ", end="  ")
        ajustador_texto = 20 - len(str(lista_claves[i]))
        print(lista_claves[i].upper() + ajustador_texto * " ", end="  ")

    print("\n" + "-" * 21 * (len(lista_claves) + 1) + "\n")

    for id_pedido in PEDIDOS:
        lista_pedidos = list(PEDIDOS[id_pedido].values())
        ajustador_texto = 20 - len(str(id_pedido))
        print(str(id_pedido) + ajustador_texto * " ", end="  ")

        for i in range(len(lista_pedidos)):
            ajustador_texto = 20 - len(str(lista_pedidos[i]))
            print(str(lista_pedidos[i]) + ajustador_texto * " ", end="  ")
        print("\n")


imprimir_diccionario_compuesto(PEDIDOS, 1)
imprimir_diccionario_compuesto_tabla(PEDIDOS, "pedidos")
print("\n\n")


'''-------------------------------------------------------------------'''

# INGRESAR DATOS EN UN DICCIONARIO

clientes = {
    40000005: {
        "nombre": "Carlos Mario",
        "apellido": "Juarez Palacios",
        "edad": 27,
        "fecha_ingreso": "27/12/2019"
    },
    40000006: {
        "nombre": "Juliana",
        "apellido": "Antonianni",
        "edad": 35,
        "fecha_ingreso": "27/12/2019"
    },
}


def alta_cliente(clientes: dict) -> None:

    # Generamos una clave para el nuevo cliente
    dni_cliente = int(input("Ingrese su DNI >>>   "))

    # Ingresamos los datos del cliente (deberíamos verficar por cada dato que sea correcto)
    nombre = input("Ingrese su nombre >>>   ")
    apellido = input("Ingrese su apellido >>>   ")
    edad = int(input("Ingrese su edad >>>   "))
    fecha_ingreso = input("Ingrese su fecha de ingreso >>>   ")

    # Creamos un cliente
    cliente_nuevo = dict()

    # Insertamos los datos que ingresó el cliente
    cliente_nuevo["nombre"] = nombre
    cliente_nuevo["apellido"] = apellido
    cliente_nuevo["edad"] = edad
    cliente_nuevo["fecha_ingreso"] = fecha_ingreso

    # Insertamos en la lista de clientes al nuevo cliente con su respectiva clave
    clientes[dni_cliente] = cliente_nuevo


def baja_cliente(clientes: list) -> None:
    borrar_clientes = True

    while borrar_clientes:
        imprimir_diccionario_compuesto_tabla(clientes, "clientes")

        id_cliente = int(input("Seleccione el cliente que desea borrar (por DNI) >>>   "))

        if id_cliente in clientes:
            clientes.pop(id_cliente)
            print(f"Se ha borrado el cliente {id_cliente} con éxito.")
        else:
            print(f"El cliente {id_cliente} no existe.")
        
        if input("¿Desea seguir borrando clientes? (SI / NO)") == "NO": borrar_clientes = False


baja_cliente(clientes)
imprimir_diccionario_compuesto_tabla(clientes, "clientes")






'''
Observar que:
* for clave in diccionario: print(clave)  -->  ITERA LAS CLAVES
* for clave in diccionario: print(diccionario[clave])  -->  ITERA LOS VALORES DE LAS CLAVES

* for clave in diccionario: for clave2 in diccionario[clave]: print(clave2)  -->  ITERA LAS CLAVES DE CADA SUBDICCIONARIO
* for clave in diccionario: for clave2 in diccionario[clave]: print(diccionario[clave][clave2]  -->  ITERA LOS VALORES DE CADA SUBDICCIONARIO

* for clave in diccionario: for clave2 in clave: print(clave2)  -->  ARROJA ERROR DE ITERAR SOBRE INT


>>>>> OTROS COMANDOS <<<<<
diccionario.keys()          -->  DEVUELVE TODAS LAS CLAVES DEL DICCIONARIO
diccionario.values()        -->  DEVUELVE TODOS LOS VALORES DEL DICCIONARIO
diccionario.items()         -->  DEVUELVE EL DICCIONARIO COMPLETO
diccionario.get(clave,[])   -->  DEVUELVE EL VALOR DE LA CLAVE, O [] SI NO EXISTE LA CLAVE
diccionario.clear()         -->  ELIMINA TODo EL DICCIONARIO
diccionario.pop(clave)      -->  ELIMINA UNA CLAVE Y RETORNA SU VALOR
diccionario.copy()          -->  DEVUELVE UNA COPIA DEL DICCIONARIO ORIGINAL
zip()                       -->  RECIBE DOS ITERABLES Y JUNTA EL ELEMENTO i DE UNO CON EL ELEMENTO i DEL OTRO EN UN dict()
diccionario.update()        -->  RECIBE UN dict() COMO PARÁMETRO; "PISA" LAS CLAVES EXISTENTES Y AGREGA LAS NUEVAS

--- USO: claves_dic = list(diccionario.keys())  ---
'''
