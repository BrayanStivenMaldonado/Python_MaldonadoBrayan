#Entrada para que el usuario ponga los números
entrada = input("Numeros: ")

#Comando para que los valores se agreguen a la lista y estén separados por la ","
lista = list(sorted(set(map(int, entrada.split(",")))))

#Entrada para que el usuario ponga el objetivo
target = int(input("Target: "))

#Tamaño de la lista, para darselo como parámetro al ciclo for
tamaño = len(lista)

#Si el objetivo está en la lista, se imprime la posición en la que lo encuentra
if target in lista:       
    for i in range (0,tamaño):     
        if target == lista[i]:
            print(i)
            break
#Si el objetivo no está en la lista, se agrega el valor del target a la lista y se vuelve a ordenar y se imprime la posición en la que queda
if target not in lista:
    lista.append(target)
    lista.sort()
    tamaño2 = len(lista)
    for i in range (0,tamaño2):        
            if target == lista[i]:
                print(i)
                break
            
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470                