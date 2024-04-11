#Adivinar el número aleatorio que genera el programa y felicita al jugador cuando gana

print("   BIENVENIDO AL JUEGO DE ADIVINAR EL NUMERO ALEATORIO")
print("""1). Tu objetivo va a ser adivinar el número en la menor cantidad de intentos
2). Cada vez que hagas una suposición te voy a dar una pista
3). Tienes 10 intentos para lograrlo
3). Cuando lo logres, te saldrá una felicitación y se dirá en cuántos intentos lo lograste
""")
import random
aleatorio = random.randint(1,100)
print(aleatorio)
for i in range(1,11):
    print("Ingrese un número del 1 al 100   Intento:",(i))
    numero= int(input(""))
    if numero==aleatorio:
        print("!Felicidades¡, has ganado el juego en",(i),"intentos")
        break
    if numero!=aleatorio:
        if numero>aleatorio:
            print("Pista: El número es más pequeño")
            print("")
        else:
            print("Pista: El número es más grande")
            print("")
    if i==10:
        print("Lo siento, se te han acabado las oportunidades para intentar adivinar")
        
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470