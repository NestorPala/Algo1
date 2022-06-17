# RECUPERATORIO DEL 1ER PARCIAL DE ALGORTIMOS Y PROGRAMACIÓN I
# ALUMNO: PALAVECINO ARNOLD, NESTOR FABIAN
# ---------------------------------------------------------------------------------------------------------------------

# EJERCICIO 4


def total_a_pagar(productos_volteados: str, verduleria: dict):
    productos = productos_volteados.split(" ")
    productos2 = dict() # productos2 = {"T": 3, "P": 5,}
    total = 0

    for elemento in productos:
        productos2[elemento[1:2:1]] = elemento[0:1:1]

    for elemento in productos2:
        total += verduleria[elemento] * int(productos2[elemento])
    
    return total


def main() -> None:
    verduleria = {
        "T": 35,
        "B": 20,
        "K": 70,
        "M": 30,
        "P": 25
    }

    productos_volteados = "3T 5P 2M 6B 2K"
    
    print(total_a_pagar(productos_volteados, verduleria))


main()

