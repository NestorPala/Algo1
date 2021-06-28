"""
Realizar un programa que permita jugar a adivinar un número entero.
El participante A elige el número a adivinar y luego hace jugar al participante B,
el cual deberá intentar adivinarlo arriesgando números.
El programa debe guiar al participante B indicándole, en cada intento,
si el número arriesgado es mayor o menor al definido por el participante A.
El juego debe concluir al acertar el número o superar los 20 intentos.
Al acertar el número debe indicar la cantidad de intentos que fueron utilizados para lograrlo.
En caso de no haber conseguido el objetivo, debe indicarle que ha superado los 20 intentos.
"""

numerosecreto = input("JUGADOR A, ELIJA UN NUMERO   >>>  ")
print("")
print("")


print("JUGADOR B, ADIVINE EL NUMERO ")


iterador = 0
rango = 20
intentos = 0


while iterador < rango:
    
    print("")
    print("(INTENTOS RESTANTES:", 20-iterador, ")")
    numerosugerido = input(">>>   ")
    print("")
    
    iterador += 1
    
    if numerosugerido < numerosecreto:
        print("EL NUMERO ARRIESGADO ES MENOR AL NUMERO SECRETO")
        intentos += 1
        
    if numerosugerido > numerosecreto:
        print("EL NUMERO ARRIESGADO ES MAYOR AL NUMERO SECRETO")
        intentos += 1
        
    if (intentos == rango):
        print("")
        print("FALLASTE", rango, "VECES PA, DALE, MEDIA PILA")
         
    if numerosugerido == numerosecreto:
        print("GANASTE")
        print("NUMERO DE INTENTOS UTILIZADOS: ", iterador)
        iterador = rango
        