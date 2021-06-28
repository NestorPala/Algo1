
a = ""
min = 0
max = 0
iniciado = False


while a != "salir":
    num = input("INGRESE UN NUMERO O ESCRIBA 'salir' PARA SALIR  >>>  ")
    
    if num != "salir":
        numero = int(num)
    else:
        a = "salir"
    
    if iniciado == False:
        min = numero
        max = numero
        iniciado = True
        
    if numero < min:
        min = numero
        
    if numero > max:
        max = numero


print("EL NUMERO MÍNIMO ES", min)
print("EL NUMERO MÁXIMO ES", max)  
