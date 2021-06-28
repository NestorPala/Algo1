'''
2) BÚSQUEDA DE LA LETRA
Se deberá crear un programa que permita:
Ingresar una palabra y una letra a buscar.
Se deberá buscar la letra en esa palabra; en caso de que esté, se imprimirá: "LA ENCONTRÉ", caso contrario: "PSS, NO 'STABA".
'''

##############################################

palabra = input("INGRESE UNA PALABRA   >>>   ")
letra = input("INGRESE UNA LETRA PARA BUSCAR EN LA PALABRA ANTERIOR   >>>   ")

'''(Vamos a suponer que el usuario ingresa una sola letra,
porque sino habría que meter el segundo input dentro de un while de comprobación)'''

##############################################

if (letra in palabra):
    print("LA ENCONTRÉ")
else:
    print("PSS, NO 'STABA")