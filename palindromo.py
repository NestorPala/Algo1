
def es_palindromo(palabra: str) -> None:
    letras_palabra = list()
    palindromo = True
    caracteres_malos = " |°¬!#$%&/()=?¡;:_|@·~{[]}\·¿,.-+<>"

    for letra in palabra:
        if letra not in caracteres_malos:
            letras_palabra.append(letra.lower())

    a = len(letras_palabra)
    
    for i in range(a):
        if letras_palabra[i] != letras_palabra[(a-1) - i]:
            palindromo = False

    if palindromo: 
        print("La palabra o frase es un palindromo")
    else:
        print("La palabra o frase NO es un palindromo")


def main() -> None:
    palabra = "A Mercedes, ese de crema."
    es_palindromo(palabra)


main()
