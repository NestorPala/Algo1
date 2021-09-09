
def ingresar_contrasenia(min_caracteres: int = 8, max_caracteres: int = 14, caracteres_especiales: bool = False) -> str:
    contrasenia = str()

    while not min_caracteres <= len(contrasenia) <= max_caracteres  or  contrasenia.isalnum() == caracteres_especiales:

        print(f"Ingrese una contraseña de entre {min_caracteres} y {max_caracteres} caracteres")
        if not caracteres_especiales: print("(No se permiten caracteres especiales, ej: +#$¿-_,.%=)")

        contrasenia = input("\n>>>  ")

    return contrasenia


def main() -> None:
    contrasenia = ingresar_contrasenia()
    print(f"\nLa contraseña ingresada es: {contrasenia}")


main()




