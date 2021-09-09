# TP1 DE ALGORITMOS Y PROGRAMACIÓN I
# PALAVECINO ARNOLD, NESTOR FABIAN
# ------------------------------------------------------------------


from random import random, randrange, shuffle
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


def ingresar_nombre(num_jugador: int) -> str:
    '''
    PRE: --
    POST: Devuelve un string en minúsculas sin caracteres especiales
    '''
    nombre = input(f"Ingrese el nombre del jugador {num_jugador}:   ")
    while not (nombre != "" and nombre.isalpha()):
        nombre = input(f"Por favor, ingrese un nombre para el jugador {num_jugador}:   ")
    return nombre.lower()


def configurar_tableros(tablero1: list, tablero2: list, tamanio_tablero: int) -> None:
    '''
    PRE: El tamaño de los tableros tiene que ser mayor a cero
    POST: Los tableros se van llenos con listas de listas vacías
    DESC: Crea 2 tableros y los inicializa
    '''
    tablero1.clear()
    tablero2.clear()
    for i in range(tamanio_tablero):
        tablero1.append([])
        tablero2.append([])
        for j in range (tamanio_tablero):
            tablero1[i].append([])
            tablero2[i].append([])
    

def obtener_palabras() -> list:
    palabras = ["Amarillo", "Armadillo", "Auriculares", "Bart", "Blanco", "Celeste", "Chinchilla", "Círculo",
            "Cooler", "CPU", "Cuadrado", "Discord", "Elefante", "Facebook", "Flanders", "Foca", "Fuente",
            "Gabinete", "GPU", "Gris", "Guepardo", "HDD", "Hexágono", "Hiena", "Homero", "Hormiga", "Instagram",
            "Lisa", "Maggie", "Mantarraya", "Marge", "Mariposa", "Marrón", "Meet", "Micrófono", "Molusco", "Monitor",
            "Mosca", "Motherboard", "Mouse", "Naranja", "Negro", "Octágono", "Oso", "Óvalo", "Paralelogramo", "Parlantes",
            "Pato", "Pavo", "Pendrive", "Pentágono", "Perdiz", "Perico", "Polilla", "RAM", "Rojo", "Romboide", "Rosa",
            "Saltamontes", "Skype", "Slack", "SSD", "Teclado", "Telegram", "Tigre", "Trapecio", "Triángulo", "Twitter",
            "Vaca", "Violeta", "WhatsApp", "Zoom"]
    return palabras


def rellenar_tablero(tablero: list) -> None:
    '''
    PRE: El tamaño del tablero es mayor a cero.
    POST: El tablero queda lleno de pares de palabras. Todas las palabras están distribuidas de manera aleatoria.
    '''
    tamanio_tablero = len(tablero)
    palabras = obtener_palabras()
    palabras_ingresadas = list()
    cant_palabras_distintas = 0
    max_palabras_distintas = (1/2)*tamanio_tablero**2
  
    while cant_palabras_distintas < max_palabras_distintas:
        palabra_nueva = palabras[randrange(0, len(palabras), 1)]

        if palabra_nueva not in palabras_ingresadas:
            palabras_ingresadas.append(palabra_nueva)
            cant_palabras_distintas += 1
            
    palabras_ingresadas.extend(list(palabras_ingresadas))
    shuffle(palabras_ingresadas)
    
    for i in range(tamanio_tablero):
        for j in range (tamanio_tablero):
            tablero[i].insert(j, palabras_ingresadas.pop())


def mostrar_tablero(nombre: str, tablero: list, coordenadas: list) -> None:
    '''
    PRE: El tamaño del tablero es mayor a cero, las coordenadas están definidas
    POST: Muestra el tablero del jugador por pantalla
    '''
    tamanio_tablero = len(tablero)
    mostrar_coordenadas_letras = True

    print(f"------------------- TABLERO DEL JUGADOR '{nombre}' -------------------\n")
    for i in range(tamanio_tablero):
        if mostrar_coordenadas_letras:
            print("", end="\t")
            for letra in range(tamanio_tablero):
                print(coordenadas[letra].upper(), end="    ")
            print("\n\n")
            mostrar_coordenadas_letras = False

        print(i+1, end="\t")

        for j in range(tamanio_tablero):
            '''
            # MODO CORRECCIÓN DE FALLOS (MUESTRA LAS PALABRAS EN VEZ DE "X")
            if tablero[i][j] != None:
                ajustador_texto = " " * (13 - len(tablero[i][j]))
            else:
                ajustador_texto = " " * 9
            print(f"{tablero[i][j]}{ajustador_texto}", end="\t")
            '''
            if tablero[i][j] != None:
                print("X", end="    ")
            else:
                print(" ", end="    ")
            
        print("\n")


def trasponer_tablero(tablero_victima: list) -> None:
    '''
    PRE: El tamaño del tablero es mayor a cero
    POST: El tablero queda traspuesto
    '''
    traspuesta = list()

    for i in range(len(tablero_victima)):
        traspuesta.append([])
        for j in range(len(tablero_victima)):
            traspuesta[i].append([])

    for i in range(len(tablero_victima)):
        for j in range(len(tablero_victima)):
            traspuesta[i][j] = tablero_victima[j][i]

    for i in range(len(tablero_victima)):
        for j in range(len(tablero_victima)):
            tablero_victima[i][j] = traspuesta[i][j]


def espejar_tablero(tablero_victima: list) -> None:
    '''
    PRE: El tamaño del tablero es mayor a cero
    POST: El tablero queda espejado de forma vertical u horizontal
    '''
    espejada = list()
    dado = randrange(1,3,1)
    #dado = 1 --> Espejado horizontal; dado = 2 --> Espejado vertical

    for i in range(len(tablero_victima)):
        espejada.append([])
        for j in range(len(tablero_victima)):
            espejada[i].append([])

    if dado == 1:
        for i in range(len(tablero_victima)):
            for j in range(len(tablero_victima)):
                espejada[i][j] = tablero_victima[i][len(tablero_victima)-1-j]
    else:
        for i in range(len(tablero_victima)):
            for j in range(len(tablero_victima)):
                espejada[i][j] = tablero_victima[len(tablero_victima)-1-i][j]

    for i in range(len(tablero_victima)):
        for j in range(len(tablero_victima)):
            tablero_victima[i][j] = espejada[i][j]


def tirar_dado(jugador: list, probabilidades: list) -> bool:
    '''
    PRE: Las probabilidades están entre 0.0 y 1.0
    POST: La lista jugador queda con el valor modificado en [4], [5], [6] o [7] o ninguna
    DESC: Devuelve un booleano indicando si sale o no una carta, y agrega la carta en caso de que salga

        Cartas del juego  ->  1: Replay, 2: Layout, 3: Toti, 4: Fatality
        dado_carta: decide la carta a sacar
        dado_obtiene: decide si se entra en el rango de probabilidades de la carta elegida
        probabilidades[]: en la lista de los Ajustes 'parametros_juego[]', las probabilidades de las cartas están en las posiciones 1,2,3,4
        jugador[]: las cartas se "almacenan" en las posiciones 4,5,6,7 [3 + (1,2,3,4)]
    '''
    dado_carta = randrange(1,5,1)
    dado_obtiene = random()
    if dado_obtiene <= probabilidades[dado_carta]:
        jugador[3 + dado_carta] += 1
        return True
    else:
        return False


def mostrar_mensaje_carta(carta: int) -> None:
    limpiar_pantalla()
    if carta == 1:
        print("°°° ¡REPLAY! ¡REPLAY! °°°")
        print("°°° Usted tendrá un nuevo turno si falla °°°\n\n")
    elif carta == 2:
        print("°°° ¡USTED ACABA DE MEZCLAR EL TABLERO DEL RIVAL! °°°")
        print("°°° Las posiciones que su rival recordaba ya no le sirven más °°°\n\n")
    elif carta == 3:
        print("°°° ¡USTED HA HECHO LA GRAN 'TOTI'! °°°")
        print("°°° Ahora su rival deberá utilizar un espejo para jugar :P °°°\n\n")
    else:
        print("°°°  F A T A L I T Y  °°°")
        print("°°° Usted acaba de trasponer el tablero de su adversario, ¡lo dio vuelta como una media! °°°\n\n")   
    

def jugar_carta(jugador: list, jugador_victima: list, rejugar: bool) -> None:
    '''
    PRE: Tamaño tablero_victima mayor a cero. rejugar = False.
    POST: Variable tablero_victima modificada
    DESC: Permite al jugador jugar una carta especial en caso de decidir hacerlo al inicio de su turno
    '''
    tablero_victima = jugador_victima[1]
    
    print("Elija la carta que desea jugar (1, 2, 3, o 4) >>>   ")
    opcion = ingresar_opcion(4)
    if jugador[opcion + 3] == 0:
        while jugador[opcion + 3] == 0:
            print("No existe esa carta en el inventario, por favor, elija otra")
            opcion = ingresar_opcion(4)

    if opcion == 1:
        rejugar = True
    elif opcion == 2:
        shuffle(tablero_victima)
    elif opcion == 3:
        espejar_tablero(tablero_victima)
    else:
        trasponer_tablero(tablero_victima)

    mostrar_mensaje_carta(opcion)
    
    if opcion != 1: jugador_victima[8] = opcion
    jugador[opcion + 3] -= 1
    return rejugar


def manejar_cartas(jugador: list, tablero_victima: list, carta: bool) -> bool:
    '''
    PRE: Tablero_victima mayor a cero, el jugador tiene que tener los valores de sus cartas acumuladas
    POST: Se modifica la variable rejugar (manejada por la carta "Replay"), se modifica tablero_victima
    DESC: Permite al usuario elegir si quiere jugar o no una carta, y luego elegir qué carta jugar mediante jugar_carta()
    '''
    rejugar = False
    print(f"ES EL TURNO DEL JUGADOR: '{jugador[0]}'\n")

    if jugador[8] != 0:
        print("\n>>>>> SU RIVAL LE HA APLICADO LA CARTA: ", end="")
        if jugador[8] == 2: print("'LAYOUT' <<<<<\n\n") 
        elif jugador[8] == 3: print("'TOTI' <<<<<\n\n")
        elif jugador[8] == 4: print("'FATALITY' <<<<<\n\n")
        jugador[8] = 0

    if carta: print("Has recibido una carta!", end="\n\n")

    if jugador[4] > 0 or jugador[5] > 0 or jugador[6] > 0 or jugador[7] > 0:
        print(f"----------INVENTARIO DE CARTAS COMODÍN DEL JUGADOR: '{jugador[0]}'----------\n")    
        print(f"(1) 'Replay': {jugador[4]}\n(2) 'Layout': {jugador[5]}\n(3) 'Toti': {jugador[6]}\n(4) 'Fatality': {jugador[7]}\n")
        print("\n¿Desea jugar una carta? (1:  SI | 2:  NO) >>>   ")
        opcion = ingresar_opcion(2)
        if opcion == 1:
            rejugar = jugar_carta(jugador, tablero_victima, rejugar)
        else:
            limpiar_pantalla()
            print("Usted decidió no utilizar una carta\n\n")
    else:
        print("Usted no posee cartas disponibles para jugar", end="\n\n")
            
    return rejugar


def comparar_fichas(ficha1: list, ficha2: list, jugador: list, coincidencia: bool, rejugar: bool) -> tuple:
    '''
    PRE: Formato string ficha ej. "a5". El jugador tiene que tener su tablero con tamaño mayor a cero
    POST: Modifica el tablero del jugador
    DESC: Permite al juego comparar las dos fichas elegidas por el usuario para ver si son iguales
    '''
    # FICHA = [ficha_nombre, ficha_coordenada1, ficha_coordenada2, contenido]
    if ficha1[3] == ficha2[3]:
        limpiar_pantalla()
        if ficha1[3] == None and ficha2[3] == None:
            print(">>>>> Las ubicaciones seleccionadas no poseen fichas, debe jugar de vuelta <<<<<\n\n")
            coincidencia = True
        else:
            #Acá guardamos el progreso del jugador
            jugador[2] += 1
            print("¡Felicidades, has encontrado dos fichas iguales!", end="\n\n")
            print(f"El contenido de las fichas {ficha1[0].upper()} y {ficha2[0].upper()} era: '{ficha1[3]}'\n\n")
            jugador[1][ ficha1[1] ][ ficha1[2] ] = None
            jugador[1][ ficha2[1] ][ ficha2[2] ] = None
    else:
        print(f"\n\n>>>>> Las fichas {ficha1[0]} y {ficha2[0]} no coinciden <<<<<\n\n")
        print(f"El contenido de la ficha {ficha1[0].upper()} es: '{ficha1[3]}' ")
        print(f"El contenido de la ficha {ficha2[0].upper()} es: '{ficha2[3]}'\n")
        if rejugar:
            coincidencia = True
            print("\n°°° ¡ENTRA EN JUEGO LA CARTA 'REPLAY'! °°°\n°°° Usted posee un nuevo turno para jugar °°°\n\n")
            rejugar = False
        else:
            coincidencia = False
    
    return coincidencia, rejugar


def levantar_ficha(ficha: str, jugador: list) -> list:
    '''
    PRE: Formato string ficha ej. "a5", tablero del jugador con tamaño mayor a cero
    POST: ---
    DESC: Recibe las coordenadas de la ficha (ej. "a5") y arma una nueva ficha más completa, ej: ["a5", 0, 4, "Elefante"]
    '''
    x = 0
    if len(ficha) == 2:
        x = 2
    if len(ficha) == 3:
        x = 3

    ficha_nombre = ficha
    ficha_coordenada1 = int(ficha[1:x:1]) - 1
    ficha_coordenada2 = ord(ficha[0:1:1].lower()) - 97
    contenido = jugador[1][ficha_coordenada1][ficha_coordenada2]
    
    return [ficha_nombre, ficha_coordenada1, ficha_coordenada2, contenido]


def ingresar_ficha(num_ficha: int, ficha_anterior: str, coordenadas: list, tamanio_tablero: int) -> str:
    '''
    PRE: Tamaño tablero mayor a cero
    POST: ---
    DESC: Permite ingresar las coordenadas de las fichas del tablero a levantar.
    '''
    x = 0
    ficha = ""

    while (ficha.isalnum() == False 
            or (len(ficha) != 2 and len(ficha) != 3)
            or ficha[0:1:1].lower() not in coordenadas
            or ficha[1:x:1].isnumeric() == False
            or (1 <= int(ficha[1:x:1]) <= tamanio_tablero) == False
            or ficha == ficha_anterior
            ):
        ficha = input(f"Por favor, ingrese las coordenadas para la ficha {num_ficha} (LETRA NÚMERO) >>>    ")

        if len(ficha) == 2:
            x = 2
        if len(ficha) == 3:
            x = 3

    # ejemplo: ficha = "a5" o "g12" (coordenadas LETRA-NÚMERO)
    return ficha


def ingresar_fichas(coordenadas: list, tamanio_tablero: int) -> tuple:
    '''
    PRE: ---
    POST: ---
    DESC: Permite ingresar las coordenadas de las fichas del tablero a levantar.
    '''
    ficha1 = ingresar_ficha(1, " ", coordenadas, tamanio_tablero)
    ficha2 = ingresar_ficha(2, ficha1, coordenadas, tamanio_tablero)
            
    return ficha1, ficha2


def manejar_fichas(jugador: list, rejugar: bool) -> bool:
    '''
    PRE: Jugador posee tablero con tamaño mayor a cero
    POST: Modifica el tablero del jugador, modifica parámetros de continuidad del juego
    DESC: Permite al jugador ver su tablero y levantar las fichas para ver si son iguales
    '''
    coordenadas_max = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
    coordenadas = list()
    tamanio_tablero = len(jugador[1])
    coincidencia = True
    jugando = True
    
    for i in range(tamanio_tablero):
        coordenadas.append(coordenadas_max[i])

    while coincidencia:
        mostrar_tablero(jugador[0], jugador[1], coordenadas)
        print(f"Es el turno de jugar de: '{jugador[0]}'")
        x1, x2 = ingresar_fichas(coordenadas, tamanio_tablero)
        ficha1 = levantar_ficha(x1, jugador)
        ficha2 = levantar_ficha(x2, jugador)
        coincidencia, rejugar = comparar_fichas(ficha1, ficha2, jugador, coincidencia, rejugar)
        
        if jugador[2]/(tamanio_tablero/2) == tamanio_tablero:
            coincidencia = False
            jugando = False
            jugador[3] = True
            print(">>>>> ¡FELICIDADES, HAS GANADO LA PARTIDA! <<<<<")

    print("\n\nPulse 1 para continuar")
    salir = ingresar_opcion(1)
    return jugando


def terminar_partida(jugador1: list, jugador2: list, ganadores: list) -> None:
    '''
    PRE: Que haya terminado la partida 
    POST: Modifica la lista de ganadores agregando el nombre del nuevo ganador
    '''
    if jugador1[3] == True:
        ganador = jugador1[0]
    else:
        ganador = jugador2[0]

    print(f"EL GANADOR DE ESTA PARTIDA ES: '{ganador.upper()}'")

    if len(ganadores) == 4:
        ganadores.clear()
        ganadores.append(ganador)
    else:
        ganadores.append(ganador)
        
    print("\n\nPulse 1 para volver al menú del juego")
    salir = ingresar_opcion(1)


def jugar(jugador1: list, jugador2: list, parametros_juego: list) -> None:
    '''
    PRE: Jugadores con todos los parámetros definidos
    POST: Tableros de los jugadores modificados
    DESC: Maneja el núcleo principal del juego (dado, cartas, fichas, turnos)
    '''
    turno_jugador1 = True
    jugando = True
    jugador = list()
    victima = list()
    '''
    jugador1 - nombre1  -->  Juega en: tablero2, Modifica: tablero1
    jugador2 - nombre2  -->  Juega en: tablero1, Modifica: tablero2
    '''   
    while jugando:
        if turno_jugador1:
            jugador = jugador1
            victima = jugador2
        else:
            jugador = jugador2
            victima = jugador1

        carta = tirar_dado(jugador, parametros_juego)
        rejugar = manejar_cartas(jugador, victima, carta)
        jugando = manejar_fichas(jugador, rejugar)
        turno_jugador1 = not turno_jugador1
        limpiar_pantalla()


def inicializar_juego(tamanio_tablero: int) -> tuple:
    '''
    PRE: Tamaño del tablero mayor a cero
    POST: Los jugadores poseen todos sus parámetros de juego
    DESC: Inicializa el juego (crea los tableros, los jugadores y asigna los tableros a los jugadores)
    '''
    tablero1 = list()
    tablero2 = list()
    nombre1 = ingresar_nombre(1)
    nombre2 = nombre1

    while nombre2 == nombre1:
        nombre2 = ingresar_nombre(2)
        if nombre2 == nombre1:
            print("Los nombres de los dos jugadores no pueden ser iguales")

    ''' jugadorX = [nombre, tablero_correspondiente, cantidad_pares_encontrados, ganador:true/false, 
                    cantidad_replay, cantidad_layout, cantidad_toti, cantidad_fatality, ataque_rival: 2, 3 o 4] '''
    jugador1 = [nombre1, tablero2, 0, False, 0, 0, 0, 0, 0] 
    jugador2 = [nombre2, tablero1, 0, False, 0, 0, 0, 0, 0]

    limpiar_pantalla()
    configurar_tableros(tablero1, tablero2, tamanio_tablero)
    rellenar_tablero(tablero1)
    rellenar_tablero(tablero2)

    return jugador1, jugador2


def manejador_juego(parametros_juego: list, ganadores: list) -> None:
    '''
    PRE: Dentro de parametros_juego, tamaño tablero mayor a cero
    POST: Modifica la lista de ganadores
    DESC: >>>>> CONTROLA EL JUEGO (CREA LOS ELEMENTOS Y MANEJA LAS PARTIDAS) <<<<<
    '''
    tamanio_tablero = parametros_juego[0]
    jugador1, jugador2 = inicializar_juego(tamanio_tablero)
    jugar(jugador1, jugador2, parametros_juego)
    terminar_partida(jugador1, jugador2, ganadores)


def ver_ajustes_actuales(parametros_juego: list) -> None:
    '''
    PRE: --
    POST: --
    DESC: Muestra los ajustes actuales del juego al usuario
    '''
    limpiar_pantalla()
    print("Los ajustes actuales son:\n")
    print(f"Duración del juego: {parametros_juego[0]}x{parametros_juego[0]}")
    print(f"Probabilidad de la carta 'Replay': {int(parametros_juego[1]*100)}%")
    print(f"Probabilidad de la carta 'Layout': {int(parametros_juego[2]*100)}%")
    print(f"Probabilidad de la carta 'Toti': {int(parametros_juego[3]*100)}%")
    print(f"Probabilidad de la carta 'Fatality': {int(parametros_juego[4]*100)}%")
    print("\nPulse 1 para salir >>>   ")
    opcion = ingresar_opcion(1)


def ingresar_probabilidad(carta: str) -> float:
    '''
    PRE: --
    POST: Devuelve el valor de una probabilidad entre 0 y 100
    '''
    probabilidad = input(f"Ingrese la probabilidad de la carta {carta} en % (entre 0 y 100) >>>   ")
    while not (probabilidad.isnumeric() and 0 <= int(probabilidad) <= 100):
        probabilidad = input("Por favor, ingrese una probabilidad entera entre 0 y 100:  ")
    return int(probabilidad) / 100


def probabilidades_cartas(parametros_juego: list) -> None:
    '''
    PRE: --
    POST: Modifica la lista parametros_juego
    DESC: Permite configurar las probabilidades de las cartas
    '''
    limpiar_pantalla()
    print("\nProbabilidades de las cartas comodín\n")
    print("1:  Probabilidad de Replay\n2:  Probabilidad de Layout\n3:  Probabilidad de Toti\n4:  Probabilidad de Fatality\n5:  (ATRÁS)")
    opcion = ingresar_opcion(5)

    if int(opcion) == 1:
        replay = ingresar_probabilidad("Replay")
        parametros_juego[1] = replay
    if int(opcion) == 2:
        layout = ingresar_probabilidad("Layout")
        parametros_juego[2] = layout
    if int(opcion) == 3:
        toti = ingresar_probabilidad("Toti")
        parametros_juego[3] = toti
    if int(opcion) == 4:
        fatality = ingresar_probabilidad("Fatality")
        parametros_juego[4] = fatality


def duracion_juego(parametros_juego: list) -> None:
    '''
    PRE: --
    POST: Modifica la lista parametros_juego
    DESC: Permite configurar el tamaño de los tableros de los jugadores
    '''
    limpiar_pantalla()
    print("\nDuración del juego\nElija el tamaño del tablero:")
    print("1:   4 X  4 (corta duración)\n2:   8 X  8 (media duración)\n3:  12 X 12 (larga duración)\n4:  (ATRÁS)")
    opcion = ingresar_opcion(4)

    if int(opcion) == 1:
        parametros_juego[0] = 4
    if int(opcion) == 2:
        parametros_juego[0] = 8
    if int(opcion) == 3:
        parametros_juego[0] = 12


def ajustes(parametros_juego: list) -> None:
    '''
    PRE: --
    POST: Lista parametros_juego modificada
    DESC: PERMITE VER Y MODIFICAR LA CONFIGURACIÓN DEL JUEGO
    '''
    volver_al_menu = True
    while volver_al_menu:
        limpiar_pantalla()
        print("\nConfiguración de la partida\n")
        print("1:  Duración del juego\n2:  Probabilidades de las cartas comodín\n3:  Ver ajustes actuales\n4:  (ATRÁS)")
        opcion = ingresar_opcion(4)

        if int(opcion) == 1:
            duracion_juego(parametros_juego)
        if int(opcion) == 2:
            probabilidades_cartas(parametros_juego)
        if int(opcion) == 3:
            ver_ajustes_actuales(parametros_juego)
        if int(opcion) == 4:
            volver_al_menu = False


def tabla_posiciones(ganadores: list) -> None:
    '''
    PRE: --
    POST: Tabla de posiciones mostrada por pantalla
    '''
    tabla = list()
    ganadores2 = list(set(ganadores)) 

    print("------------------- Tabla de posiciones (últimas 4 partidas) -------------------")

    if ganadores != []:
        for i in range(len(ganadores2)):
            tabla.append( ( ganadores2[i], ganadores.count(ganadores2[i]) ) )

    tabla_2 = sorted(tabla, key=lambda a: a[1], reverse=True) 
    tabla_3 = list()

    for elemento in tabla_2:
        if elemento not in tabla_3:
            tabla_3.append(elemento)

    if tabla_3 != []:
        for i in range(len(tabla_3)):
            print(f"{tabla_3[i][0].upper()}\t{tabla_3[i][1]}")
    else:
        print("\n                  (No se han jugado partidas de Memotest aún)\n\n")
    
    print("\n\nPulse 1 para salir")
    salir = ingresar_opcion(1)


def menu(parametros_juego: list, ganadores: list) -> int:
    '''
    PRE: --
    POST: Parametros_juego modificada, inicia el juego o termina el programa
    '''
    limpiar_pantalla()
    print("Juego de la Memoria Extendido o 'Memotest V2'\n")
    print("1:  Comenzar una nueva partida\n2:  Mostrar tabla de posiciones\n3:  Ajustes\n4:  Salir\n")
    opcion = ingresar_opcion(4)
    if opcion != 1: limpiar_pantalla()

    if int(opcion) == 2:
        tabla_posiciones(ganadores)

    if int(opcion) == 3:
        ajustes(parametros_juego)

    return int(opcion)


def main() -> None:
    # parametros_juego = [duracion, replay, layout, toti, fatality]
    # duracion:int  >>>  4 - 8 - 12
    # replay, layout, toti, fatality: float  >>>  entre 0.0 y 1.0
    parametros_juego = [4, 0.25, 0.25, 0.25, 0.25]
    ganadores = list()

    estado_programa = 0

    while estado_programa != 4:
        estado_programa = menu(parametros_juego, ganadores)

        if estado_programa == 1:
            manejador_juego(parametros_juego, ganadores)
            estado_programa = 0

    print("\n¡Adios! ¡Nos vemos la próxima!")


main()
