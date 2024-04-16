numeros = [] #Lista en la que se van a guardar los valores que ingrese el usuario
CantVal = int(input("CantVal: ")) #Cantidad de valores que va a agregar
for i in range (CantVal): #Se repite la cantidad de veces que el usuario haya dicho
    print("val ",i,":")
    numeros.append(int(input())) #Se crea la entrada y se agrega a la lista de los números

tamaño = len(numeros) #Se saca el tamaño de la lista
target = int(input("Target: ")) #Se crea la entrada para saber cuál es el número objetivo

if tamaño >= 2 and tamaño<=10000: #Condición dada por el ejercicio
    print(numeros)
    for i in range (0,len(numeros),1): #Dependiendo de lo larga que sea la lista se van a rectificar los valores
        if len(numeros)==2:
            if numeros[i]+numeros[i+1]==target: #se le da la condición del valor de números que haya para evitar problemas
                print(i, i+1)
                break
        if len (numeros)<=3:
            if numeros[i]+numeros[i+2]==target:
                print(i,i+2)
                break
        if len (numeros)<=4:
            if numeros[i]+numeros[i+3]==target:
                print(i,i+3)
                break
        if len(numeros)<=5:
            if numeros[i]+numeros[i+4]==target:
                print(i,i+4) 
else:
    print("debe tener más de un valor")
    
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470