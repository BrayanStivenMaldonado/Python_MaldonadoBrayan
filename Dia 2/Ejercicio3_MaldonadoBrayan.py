#Adivinar el número aleatorio que genera el programa y felicita al jugador cuando gana

print("   BIENVENIDO AL JUEGO DE ADIVINAR EL NUMERO ALEATORIO")     #se le da la bienvenida al usuario y se le explica cómo funciona el juego
print("""1). Tu objetivo va a ser adivinar el número en la menor cantidad de intentos
2). Cada vez que hagas una suposición te voy a dar una pista
3). Tienes 10 intentos para lograrlo
3). Cuando lo logres, te saldrá una felicitación y se dirá en cuántos intentos lo lograste
""")
import random   #se importa la libreria "random"
aleatorio = random.randint(1,100)   #a la variable "aleatorio" se le da el valor de random.randint para que me de un valor entero al azar entre 1 y 100
for i in range(1,11):   #para i=1 hasta 11 (10 veces) hacer
    print("Ingrese un número del 1 al 100   Intento:",(i))  #se le dice al usuario que ingrese un valor del 1 al 100
    numero= int(input(""))  #se le genera la entrada para que ingrese el valpr qie considere
    if numero==aleatorio:   #si el número que ingrese es igual al aleatorio se le da el anuncio de que ganó y se le dice la cantidad de intentos que lo logró
        print("!Felicidades¡ :D, has ganado el juego en",(i),"intentos") 
        break   #si esta condición se cumple, el ciclo for se va a cerrar
    if numero!=aleatorio:   #si el número que ingrese el usuario es diferente al aleatorio se van a verificar las siguientes condiciones
        if numero>aleatorio:    #si el número que ingresa es mayor al aleatorio se le da la pista de que el número a adivinar es menor
            print("Pista: El número es más pequeño")
            print("")
        else:   #si el número que ingresa es menor al aleatorio se le da la pista de que el número a adivinar es mayor
            print("Pista: El número es más grande")
            print("")
    if i==10:   #si el intento llega al valor 10, se deja de repetir el ciclo for y se le da el anuncio de que perdió el juego y se le revela cuál era el número que debía adivinar
        print("Lo siento, se te han acabado las oportunidades para intentar adivinar")
        print("El número a secreto era:",aleatorio)
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470