CantNumeros = int(input(""))   #La cantidad de valores que desea ingresar al programa

n = [] #Lista en la que se van a guardar los valores que ingrese el usuario

T = int(input("")) #Cantidad de casos que desea realizar

k = int(input("")) #Número por el que desea dividir las parejas que se creen 

for i in range (CantNumeros): #Se va a pedur la cantidad de valores que el usuario haya elegido
    n.append(int(input("Ingrese sus valores "))) #Se agregan a la lista creada anteriormente
print(n)

contador = 0
if 1<k<100001:    
    for i in n:
        if i%k==0:
            contador = contador+1
print(contador)
                                         #No pude :c


#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470 