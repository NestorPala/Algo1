'''
Se pide hacer un programa que ingrese 8 juegos de n valores positivos cada uno.
Considerar un condiciòn de corte para el n.
Calculando el promedio de cada juego, el máximo de cada juego y el mínimo de todos los juegos.
'''


######################################################################################################33

promedio_juego1 = ""
promedio_juego2 = ""
promedio_juego3 = ""
promedio_juego4 = ""
promedio_juego5 = ""
promedio_juego6 = ""
promedio_juego7 = ""
promedio_juego8 = ""

maximo_juego1 = ""
maximo_juego2 = ""
maximo_juego3 = ""
maximo_juego4 = ""
maximo_juego5 = ""
maximo_juego6 = ""
maximo_juego7 = ""
maximo_juego8 = ""

minimo_juego1 = ""
minimo_juego2 = ""
minimo_juego3 = ""
minimo_juego4 = ""
minimo_juego5 = ""
minimo_juego6 = ""
minimo_juego7 = ""
minimo_juego8 = ""

min_max_iniciador = False
minimo_global = 0

cantidad_juegos_totales = 8
cantidad_juegos_transcurridos = 0

input_aux = 0

numero_ingresado = 0
cantidad_numeros_ingresados = 0
sumatoria_numeros_ingresados = 0

salir = False



print("USTED INGRESARÁ", cantidad_juegos_totales, "JUEGOS DE NÚMEROS")
print("SI QUIERE PASAR AL SIGUIENTE JUEGO ESCRIBA 'siguiente'")
print("SI QUIERE DEJAR DE INGRESAR JUEGOS DE NÚMEROS, INGRESE 'salir'\n\n")



while salir == False:
    print("INGRESE EL NÚMERO", cantidad_numeros_ingresados + 1, "DEL JUEGO", cantidad_juegos_transcurridos + 1)
    input_aux = input(">>>>   ")
    

    if input_aux != "salir":
        if input_aux != "siguiente":
            cantidad_numeros_ingresados += 1
            numero_ingresado = float(input_aux)

            ##################################################
            
            
            # CALCULAMOS LOS MAXIMOS Y MINIMOS            
            if min_max_iniciador == False:
                minimo = numero_ingresado
                maximo = numero_ingresado
                min_max_iniciador = True
            
            if numero_ingresado < minimo:
                minimo = numero_ingresado
                
            if numero_ingresado > maximo:
                maximo = numero_ingresado
                        
                        
            # HACEMOS LA SUMATORIA PARA CALCULAR EL PROMEDIO
            sumatoria_numeros_ingresados += numero_ingresado            
            
            
            '''
            # DEBUGGING
            print("CANTIDAD DE JUEGOS TRANSCURRIDOS:", cantidad_juegos_transcurridos + 1)
            print("NUMERO INGRESADO: ", numero_ingresado)
            print("MAXIMO: ", maximo)
            print("MINIMO: ", minimo)
            print("SUMATORIA: ", sumatoria_numeros_ingresados)
            '''
            
            
            if cantidad_juegos_transcurridos + 1 == 1:
                maximo_juego1 = maximo
                minimo_juego1 = minimo
                promedio_juego1 = sumatoria_numeros_ingresados / cantidad_numeros_ingresados
                #print(">>>>>>>>>>>>>>>>>UNO UNO UNO")
                
            if cantidad_juegos_transcurridos + 1 == 2:
                maximo_juego2 = maximo
                minimo_juego2 = minimo
                promedio_juego2 = sumatoria_numeros_ingresados / cantidad_numeros_ingresados
                #print(">>>>>>>>>>>>>>>>>DOS DOS DOS")
                
            if cantidad_juegos_transcurridos + 1 == 3:
                maximo_juego3 = maximo
                minimo_juego3 = minimo
                promedio_juego3 = sumatoria_numeros_ingresados / cantidad_numeros_ingresados
                #print(">>>>>>>>>>>>>>>>>TRES TRES TRES")
            
            if cantidad_juegos_transcurridos + 1 == 4:
                maximo_juego4 = maximo
                minimo_juego4 = minimo
                promedio_juego4 = sumatoria_numeros_ingresados / cantidad_numeros_ingresados
                #print(">>>>>>>>>>>>>>>>>CUATRO CUATRO CUATRO")
                
            if cantidad_juegos_transcurridos + 1 == 5:
                maximo_juego5 = maximo
                minimo_juego5 = minimo
                promedio_juego5 = sumatoria_numeros_ingresados / cantidad_numeros_ingresados
                #print(">>>>>>>>>>>>>>>>>CINCO CINCO CINCO")
                
            if cantidad_juegos_transcurridos + 1 == 6:
                maximo_juego6 = maximo
                minimo_juego6 = minimo
                promedio_juego6 = sumatoria_numeros_ingresados / cantidad_numeros_ingresados
                #print(">>>>>>>>>>>>>>>>>SEIS SEIS SEIS")
                
            if cantidad_juegos_transcurridos + 1 == 7:
                maximo_juego7 = maximo
                minimo_juego7 = minimo
                promedio_juego7 = sumatoria_numeros_ingresados / cantidad_numeros_ingresados
                #print(">>>>>>>>>>>>>>>>>SIETE SIETE SIETE")
                
            if cantidad_juegos_transcurridos + 1 == 8:
                maximo_juego8 = maximo
                minimo_juego8 = minimo
                promedio_juego8 = sumatoria_numeros_ingresados / cantidad_numeros_ingresados
                #print(">>>>>>>>>>>>>>>>>OCHO OCHO OCHO")
            
            ##################################################
        else:
        
            cantidad_juegos_transcurridos += 1
            cantidad_numeros_ingresados = 0
            maximo = 0
            minimo = 0
            sumatoria_numeros_ingresados = 0
            min_max_iniciador = False
            
            
            if cantidad_juegos_transcurridos == cantidad_juegos_totales:
                salir = True
                
            print("---------------------------------------------")
    else:
        salir = True
            



print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/\n\n")

for i in range(cantidad_juegos_totales):
          
    if i+1 == 1:
        if maximo_juego1 != "":
            print("EL MAXIMO DEL JUEGO", i+1, "ES")
            print(maximo_juego1)
        
        if promedio_juego1 != "":
            print("EL PROMEDIO DEL JUEGO", i+1, "ES")
            print(promedio_juego1)
        
    if i+1 == 2:
        if maximo_juego2 != "":
            print("EL MAXIMO DEL JUEGO", i+1, "ES")
            print(maximo_juego2)
        
        if promedio_juego2 != "":
            print("EL PROMEDIO DEL JUEGO", i+1, "ES")
            print(promedio_juego2)
        
    if i+1 == 3:
        if maximo_juego3 != "":
            print("EL MAXIMO DEL JUEGO", i+1, "ES")
            print(maximo_juego3)
            
        if promedio_juego3 != "":
            print("EL PROMEDIO DEL JUEGO", i+1, "ES")
            print(promedio_juego3)
        
    if i+1 == 4:
        if maximo_juego4 != "":
            print("EL MAXIMO DEL JUEGO", i+1, "ES")
            print(maximo_juego4)

        if promedio_juego4 != "":
            print("EL PROMEDIO DEL JUEGO", i+1, "ES")
            print(promedio_juego4)
        
    if i+1 == 5:
        if maximo_juego5 != "":
            print("EL MAXIMO DEL JUEGO", i+1, "ES")
            print(maximo_juego5)
        
        if promedio_juego5 != "":
            print("EL PROMEDIO DEL JUEGO", i+1, "ES")
            print(promedio_juego5)
        
    if i+1 == 6:
        if maximo_juego6 != "":
            print("EL MAXIMO DEL JUEGO", i+1, "ES")
            print(maximo_juego6)
            
        if promedio_juego6 != "":
            print("EL PROMEDIO DEL JUEGO", i+1, "ES")
            print(promedio_juego6)
        
    if i+1 == 7:
        if maximo_juego7 != "":
            print("EL MAXIMO DEL JUEGO", i+1, "ES")
            print(maximo_juego7)
            
        if promedio_juego7 != "":
            print("EL PROMEDIO DEL JUEGO", i+1, "ES")
            print(promedio_juego7)
        
    if i+1 == 8:
        if maximo_juego8 != "":
            print("EL MAXIMO DEL JUEGO", i+1, "ES")
            print(maximo_juego8)
            
        if promedio_juego8 != "":
            print("EL PROMEDIO DEL JUEGO", i+1, "ES")
            print(promedio_juego8)
        
    
print("")
print("")


print("EL MINIMO GLOBAL ES")


if minimo_juego1 != "":
    minimo_global = minimo_juego1

if minimo_juego2 != "":
    if minimo_juego2 < minimo_global:
        minimo_global = minimo_juego2
        
if minimo_juego3 != "":
    if minimo_juego3 < minimo_global:
        minimo_global = minimo_juego3
        
if minimo_juego4 != "":
    if minimo_juego4 < minimo_global:
        minimo_global = minimo_juego4

if minimo_juego5 != "":
    if minimo_juego5 < minimo_global:
        minimo_global = minimo_juego5
        
if minimo_juego6 != "":
    if minimo_juego6 < minimo_global:
        minimo_global = minimo_juego6
        
if minimo_juego7 != "":
    if minimo_juego7 < minimo_global:
        minimo_global = minimo_juego7
        
if minimo_juego8 != "":
    if minimo_juego8 < minimo_global:
        minimo_global = minimo_juego8


print(minimo_global)
