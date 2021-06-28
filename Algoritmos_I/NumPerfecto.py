'''
Un número perfecto es aquel número que es igual a la suma de todos
sus divisores positivos excepto el mismo.
El primer número perfecto es 6, ya que 1+2+3=6.
Escribir un programa que muestre todos los números perfectos
hasta un número dado por el usuario.
Ayuda:
Entre 0-10.000 hay solo 3 números perfectos.
'''


num = int(input("OBTENER NÚMEROS PERFECTOS HASTA UN DETERMINADO VALOR  >>>  "))
sumadivisores = 0

for i in range (1, num+1):
    for j in range (1, i):
        if i%j==0:
#             print(i, " ES DIVISIBLE POR ", j)
            sumadivisores += j
    
    if sumadivisores == i:
        print(i, " ES UN NUMERO PERFECTO")
        
    sumadivisores = 0
            
            

