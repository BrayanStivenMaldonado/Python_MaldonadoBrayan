numeros = [] #Lista en la que se van a guardar los valores que ingrese el usuario
booleanito = True
while booleanito == True:
    n = int(input("CantVal: ")) #Entrada para saber cuántos valores va a ingresar
    if n>0 and 300>n:
        booleanito = False
    else:
        print("El valor debe estár entre 1 y 299")
        booleanito = True

for i in range (0,n):
    print("Val", i+1,":") #
    numeros.append(int(input())) #Se crea la entrada para que ingrese los valores y estos mismo se manden a la lista "numeros"
    
SinRepetidos = list(set(numeros)) #Creamos una nueva lista pero con "set" para que se eliminen los valores repetidos, ya que set es una coleccion de objetos únicos
    
print(numeros) #Se muestra la lista con todos los valores ingresados
print(SinRepetidos) #Se muestra la lista sin los valores repetidos

#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470 