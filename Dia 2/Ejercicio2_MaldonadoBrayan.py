#Adivinar el número aleatorio que genera el programa

print("   BIENVENIDO AL JUEGO DE ADIVINAR EL NUMERO ALEATORIO")
print("""1). Tu objetivo va a ser adivinar el número en la menor cantidad de intentos
2). Cada vez que hagas una suposición te voy a dar una pista
""")
import random
aleatorio = random.randint(1,100)
print(aleatorio)
for i in range(1,100):
    print("Ingrese un número del 1 al 100")
    numero= int(input(""))
    if numero==aleatorio:
        print("c:")
        break
    if numero!=aleatorio:
        if numero>aleatorio:
            print("Pista: El número es más pequeño")
        else:
            print("Pista: El número es más grande")
            
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470