#Adivinar el número aleatorio que genera el programa

print("   BIENVENIDO AL JUEGO DE ADIVINAR EL NUMERO ALEATORIO")
print("""1). Tu objetivo va a ser adivinar el número en la menor cantidad de intentos
2). Cada vez que hagas una suposición te voy a dar una pista
""") #se le da la bienvenida al usuario y se le explica cómo funciona el juego
import random #se importa la libreria "random"
aleatorio = random.randint(1,100) #a la variable "aleatorio" se le da el valor de random.randint para que me de un valor entero al azar entre 1 y 100
intentos = 0 #se le da un valor inicial a la variable "intentos" para usarlo como contador más adelante
booleanito=True
while booleanito==True: #mientras sea verdadero 
    intentos += 1 #cada vez que se repita el ciclo, el valor de "intentos" 
    print("Ingrese un número del 1 al 100, intento #",intentos)
    numero= int(input("")) #se genera la entrada para que el usuario ingrese el valor que considere
    if numero==aleatorio: #si el número ingresado por el usuario es igual al que generó el programa se le da el anuncio de que ganó
        print("Has ganado") 
        booleanito=False #y si se cumple esta condición, el programa se cierra
    if numero!=aleatorio: #si el número ingresado por el usuario es diferente al generado por el programa se verifican las siguientes condiciones
        if numero>aleatorio: #si el número ingresado es mayor al aleatorio se le da el anuncio de que debe ingresar uno más pequeño
            print("Pista: El número es más pequeño")
        else: #si el número ingresado es menor al aleatorio se le da el anuncio de que debe ingresar uno mayor
            print("Pista: El número es más grande")            
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470