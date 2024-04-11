#Estructura de Fibonacci

#se le explica al usuario el cómo funciona la estructura de Fibonacci
print("Estructura Fibonacci")
print("Se trata de una secuencia infinita de números naturales; a partir del 0 y el 1, se van sumando a pares, de manera que cada número es igual a la suma de sus dos anteriores,")
while True: #mientras sea verdadero, repetir

    cantidad =int(input("Ingrese un valor entero para saber hasta qué número se mostrará su estructura ")) #se le genera la entrada para que ingrese la cantidad de número que desea mostrar en pantalla
    a = 0
    b = 1
    print(" ")
    for i in range(1,cantidad) : #para i en rango (desde 1 a cantidad), repetir 
        while a < 89: #el valor del número 11 es 55, entonces se dice que se corten los números antes de que llegue al valor de 12, que es 89
            print(a) #Se muestra el valor de a
            break
        c = a + b #c es la suma de los valores de a y b
        a = b #a pasa a ser el valor de a
        b = c #b pasa a ser el valor de c

    r=int(input(""" 
    1). Repetir el programa  
    2). Cerrar el programa
    """))  #se le pregunta al usuario si desea volver a usar el programa, y se le genera la respectiva entrada para que ingrese la respuesta

    if r==1: #si escoge 1, el ciclo se va a volver a repetir
        print("BIENVENIDO DE NUEVO AL PROGRAMA")

    elif r==2: #si escoge el 2, se cierra el programa
        print("Nos vemos luego c:")
        break
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470