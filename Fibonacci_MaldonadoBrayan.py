print("Estructura Fibonacci")
print("Se trata de una secuencia infinita de números naturales; a partir del 0 y el 1, se van sumando a pares, de manera que cada número es igual a la suma de sus dos anteriores,")
cantidad =int(input("Ingrese un valor entero para saber hasta qué número se mostrará su estructura "))
a=0
b=1
for i in range(1,cantidad):
    while a<=89:
        print(a)
    break
c = a+b
a = b
b = c