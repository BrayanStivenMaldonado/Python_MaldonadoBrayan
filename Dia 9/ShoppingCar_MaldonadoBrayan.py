#Libreria system para usar la función ("cls")
from os import system

#Arrays en los que van a ir guardados los datos del carrito de compras.
Producto = []
Precio = []
Cantidad = []

booleanito = True
while booleanito == True: #Cada vez que salga de una opción vuelva al menú, a excepción de que desee cerrar el programa
    
    print("""
    ===== MENU DE OPCIONES =====
    1). Agregar productos al carrito
    2). Mostrar los productos dentro del carrito
    3). Cerrar el programa
        """)
    print("")
    eleccion = int(input("Ingrese el número de la opción que desea realizar: ")) #Se genera la entrada para que ingrese el número de la opción que desea realizar
    system("cls")    
    
    if eleccion == 1: #Si la elección es igual a 1, se da inicio al proceso de añadir productos al carrito de compras
        CantidadAñadir = int(input("¿Cuántos productos desea añadir? ")) #Se le pregunta la cantidad de productos que desea añadir al carrito de compras
        for i in range (0,CantidadAñadir): #Se va a repetir el proceso la cantidad de veces que el usuario lo pida
            print("Producto #",i+1)
            Producto.append(input("Ingrese el nombre del producto que desea añadir: ")) #Se le pide el nombre del producto y se agrega a la lista "Producto"
            Precio.append(input("Ingrese el precio del producto: ")) #Se le pide el precio del producto y se agrega a la lista "Precio"
            Cantidad.append(input("Ingrese la cantidad: ")) #Se le pide la cantidad del producto y se agrega a la lista "Cantidad"
            print("")
            
        input("Presione ENTER para continuar")
        system("cls")
                
    if eleccion == 2: #Si la elección es igual a 2, se da inicio al proceso de mostrar lo que se tiene dentro del carrito de compras
        if len(Producto)>=1: #Si la cantidad de productos que hay es mayor o igual a 1, se muestra lo que haya dentro del carrito de compras
            print("  CARRITO DE COMPRAS  ")
            for i in range (len(Producto)): #Ciclo for, para poder mostrar solo los contenidos de manera ordenada y no se vea como una tupla
                print("")
                print("Producto #",i+1) #El número del producto en el orden que fue agregado
                print("Nombre: ",Producto[i]),print("Precio: ",Precio[i]),print("Cantidad:",Cantidad[i]) #Se imprimen los valores del nombre, precio y cantidad de los productos que se han añadido         
        else: 
            print("No hay productos dentro del carrito") #Si la cantidad de productos que hay dentro del carro es menor que 1, se da el anuncio de que el carro está vacío
            
        print("")
        input("Presione ENTER para continuar")
        system("cls")
            
    if eleccion==3: #Si la elección es igual a 3, se cierra el programa
        print("Gracias por usar mi programa, nos vemos luego :D") #Despedida
        booleanito = False

#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470