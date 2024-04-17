#Remove Duplicates 
entrada = input()
lista = list(sorted(set(map(int, entrada.split(",")[0:300]))))
#se crea la lista, se usa el sorted para que ordene en orden ascendente, el set para eliminar los valores repetidos, el map para que me convierta en int la entrada
#y el split para que separe los valores que ingrese el usuario con el criterio de la ",".
print(lista)

#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470 