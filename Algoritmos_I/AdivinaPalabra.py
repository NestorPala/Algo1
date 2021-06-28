'''
Crear un programa que permita este funcionamiento de juego.

Un usuario1 va a ingresar una palabra y un usuario2 va a tener tres intentos para adivinar cuántas letras contiene esa palabra.

En caso de que el usuario2 adivine la cantidad; se printeará: "Muy bien!"
En caso de que el usuario2 adivine la cantidad DOS VECES; se printeará: "AH, PERO SOS BUENÍSIMOOOOO"
En caso de que el usuario2 no adivine la cantidad ninguna vez; se printeará: "Vuelva prontos; esta vez no se pudo"
'''

############################################################
'''Adivinar la palabra'''


palabra = input("USUARIO 1: POR FAVOR INGRESE UNA PALABRA   >>>   ")
largo_palabra = len(palabra)

print("\n\n\n")
print("AHORA ES EL TURNO DEL USUARIO 2")
print("\n")
print("ADIVINE CUÁNTAS LETRAS TIENE LA PALABRA INGRESADA POR EL USUARIO 1")
print("\n")

adivinar1 = int(input("INTENTO 1/3:   >>>   "))
adivinar2 = int(input("INTENTO 2/3:   >>>   "))
adivinar3 = int(input("INTENTO 3/3:   >>>   "))

############################################################

contador_adivinaciones = 0

if adivinar1 == largo_palabra:
    contador_adivinaciones += 1
    
if adivinar2 == largo_palabra:
    contador_adivinaciones += 1
    
if adivinar3 == largo_palabra:
    contador_adivinaciones += 1
    
############################################################   
    
if contador_adivinaciones == 2:
    print("AH, PERO SOS BUENÍSIMOOOOO")
    
if contador_adivinaciones == 1:
    print("Muy bien!")

if contador_adivinaciones == 0:
    print("Vuelva prontos; esta vez no se pudo")