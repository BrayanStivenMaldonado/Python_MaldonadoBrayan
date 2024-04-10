#Estructura de Fibonacci
print("Estructura Fibonacci")
print("Se trata de una secuencia infinita de números naturales; a partir del 0 y el 1, se van sumando a pares, de manera que cada número es igual a la suma de sus dos anteriores,")
#while True:
    cantidad =int(input("Ingrese un valor entero para saber hasta qué número se mostrará su estructura "))
    a = 0
    b = 1
    print(" ")
    for i in range(1,cantidad) :
        while a<=89:
            print(a)
            break
        c = a+b
        a = b
        b = c

    r=str(input("""
    1). Repetir el programa
    2). Cerrar el programa
    """))

    if r==1:
        print("BIENVENIDO DE NUEVO")
    elif r==2:
        break    
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470