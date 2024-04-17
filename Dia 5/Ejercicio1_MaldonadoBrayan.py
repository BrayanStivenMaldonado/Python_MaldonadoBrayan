#Contador de pares

def ContadorPares (n,k):
    TamañoLista = len(n) #Tamaño de la lista en la que se van a guardar los valores que ingrese el usuario
    contador = 0   #Contador para después mostrar la cantidad de las parejas que fueron válidas
    Parejas = set() #Conjunto para guardar las parejas que se creen
    Pares_sirven = [] #lista en la que se van a guardar las parejas que sean válidas

    #Bucle for para repetir las condiciones tantas veces como datos haya en la lista, para saber todos los resultados posibles
    for i in range (TamañoLista):
        for j in range (i+1, TamañoLista):
            #condicion para verificar si la suma de la pareja es divisible por el valor "k"
            if n[i] + n[j] % k == 0:
                p = tuple(sorted((n[i] , n[j])))
                if p not in Parejas:
                    Parejas.add(p)
                    Pares_sirven.append[p]
                    contador += 1
            
    return Pares_sirven , contador

#Datos que ingresa el usuario
entrada = (input("N: "))
n = [int(num) for num in entrada] #Lista en la que se van a guardar los valores que ingrese el usuario
k = int(input("k: ")) #Número por el que desea dividir las parejas que se creen 

resultado, Pares_sirven = ContadorPares(n , k)

#Mostrar los resultados obtenidos
print("Caso: ",resultado)
print("Pares: ")
for i in Pares_sirven:
    print(i)
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470 