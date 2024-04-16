numeros = [7,2,11,15]
tamaño = len(numeros)
target = int(input("Target: "))

for i in (0,tamaño-1,1):
    if numeros[i] + numeros[i+1] == target:
        print(i, i+1)
        break
    print(i, i+1)
    
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470