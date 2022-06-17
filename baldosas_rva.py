'''
En un pintoresco jardín hay un camino demarcado por baldosas de hormigón convenientemente espaciadas.
Se desea pintarlas de vivos colores habiendo elegido rojo (R), azul (A) y verde (V). 

Aprovechando que la cantidad es múltiplo de 3 se desea pintar igual cantidad con cada uno de los colores elegidos. 
Además dos baldosas consecutivas no pueden tener el mismo color.

Uno de los pintores se ha adelantado y sin consultar pintó una de las baldosas. 
Antes de proseguir con la tarea se quiere disponer de una planificación que respete las reglas indicadas y el color de la baldosa ya pintada.

Puedes colaborar escribiendo una función que haga una propuesta coherente de colores.

Dicha función recibe una cadena conteniendo una hilera formada por caracteres asterisco (*) 
y una letra A, R, V, correspondiente a la baldosa ya pintada. 
El lago de la hilera debe ser múltiplo de 3 y menor a 256. 
Cada asterisco representa una baldosa a ser pintada y esa única letra a la baldosa ya pintada indicando además su color. 
Mientras que la función devuelve una cadena que representa una hilera del mismo largo que la leída 
pero conteniendo exclusivamente letras indicando colores de baldosa.

La función debe validar la condición de entrada.

Ejemplo:
    Estado del camino antes:
    *R
    Una posible propuesta de pintado:
    VRVARA
'''


def obtener_siguiente_color(color: str):
    siguiente_color = ""

    if color == "R":
        siguiente_color = "V"
    elif color == "V":
        siguiente_color = "A"
    elif color == "A":
        siguiente_color = "R"

    return siguiente_color


def pintar_baldosas(camino: str, colores: list) -> str:
    baldosas = list()
    baldosas2 = str()
    
    for baldosa in camino:
        baldosas.append(baldosa)

    for i in range(len(colores)):
        if colores[i] in baldosas:
            color_pintado = colores[i]

    ubicacion_pintada = baldosas.index(color_pintado)
    color = color_pintado
    h = 0

    # El rango escapa de len(baldosas)-1 pero lo solucionamos con la variable h
    for i in range(ubicacion_pintada, ubicacion_pintada + len(baldosas)):

        # La lógica se simplifica bastante utilizando una función que devuelva el color a pintar
        color = obtener_siguiente_color(color)

        if i < len(baldosas) - 1:
            baldosas[i + 1] = color
        else:
            baldosas[h] = color
            h += 1
    
    # Armo el string
    for i in range(len(baldosas)):
        baldosas2 += baldosas[i]

    return baldosas2


def validar_formato_camino(camino: str, colores: list) -> bool:
    formato_correcto = True
    camino2 = list()

    for letra in camino:
        camino2.append(letra)

    # Valido que solo haya una baldosa pintada
    for i in range(len(colores)):
        if camino2.count(colores[i]) > 1:
            formato_correcto = False
    
    # Valido que haya solo asteriscos en las ubicaciones no pintadas
    if formato_correcto:
        for letra in camino2:
            if letra != "*" and letra not in colores:
                formato_correcto = False

    return formato_correcto


def main() -> None:
    colores = ["R", "V", "A"]
    camino = "*"

    while len(camino) % 3 != 0 or len(camino) >= 256 or not validar_formato_camino(camino, colores):
        camino = input("Ingrese el camino a pintar (cantidad de baldosas menor a 256 y múltiplo de 3):  ").upper()

    camino_pintado = pintar_baldosas(camino, colores)
    print(f"El camino pintado quedará así: {camino_pintado}")


main()
