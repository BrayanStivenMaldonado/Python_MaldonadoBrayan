#Llamamos a la libreria system para luego usar la opción de limpiar pantalla ("cls")
from os import system

#Diccionario en el que se van a guardar los productos del inventario
productos={
    "1001":{
        "Nombre": "Papas",
        "Precio": 3000,
        "Cantidad": 8,
    }, 
    "1002": {
        "Nombre": "Pastas",
        "Precio": 4500,
        "Cantidad": 7,
    },
    "1003": {
        "Nombre": "Arroz",
        "Precio": 4000,
        "Cantidad": 10
    }
}
#Diccionario de los precios
PreciosGeneral = {
    "1001" : 3000,
    "1002" : 4500,
    "1003" : 4000
}
#Diccionario de las cantidades
CantidadesGeneral = {
    "1001" : 8,
    "1002" : 7,
    "1003" : 10
}
#======================================================================================
#Diccionario en el que se van  a guardar los productos que se añadan al carrito de compras
CarritoCompras = {}
#Variable en la que se van a guardar los precios de los productos 
PrecioFactura = 0
#======================================================================================
#Inicio del programa

print("=====Bienvenidos a nuestra tienda=====") #Se le da la bienvenida al usuario 
print("")
print("  =====Este es nuestro catálogo=====")
print("")
print(productos) #Se le muestra la lista de prductos

booleano = True #Se crea un booleano para que se muestre el menú de opciones cada vez que termina un proceso
while booleano==True: #Se va a repetir hasta que sea verdadero
    print(""" 
    1). Agregar productos al carrito
    2). Ver el contenido del carrito
    3). Calcular el total de la compra
    4). Cerrar el programa      
    """)

    print(CarritoCompras) #Cada vez que vuelva al inicio se le va a mostrar lo que tiene dentro del carrito de compras

    r = int(input("Escoja una de las opciones de nuestro menú: "))
    if r == 1:
        booleanito = True
        while booleanito == True:
            print(productos)
            print("")
            eleccion = (input("¿Qué productos desea agregar al carrito de compras? (ingrese el ID)")) #Producto que va  agregar al carrito
            if eleccion in productos:
                CarritoCompras[eleccion] = productos[eleccion] #Se agrega la elección a la lista del carrito de compras
                CantidadAñadir = (int(input("¿Cuántas unidades desea agregar al carrito: "))) #Unidades del producto elegido que va a agregar al carrito
                condicional = True
                while condicional == True:     
                    if CantidadAñadir>0:    
                        CarritoCompras[eleccion]["Cantidad"] = CantidadAñadir
                        PrecioProducto = PreciosGeneral[eleccion]
                        PrecioFactura = PrecioFactura+((PrecioProducto)*(CantidadAñadir)) #El precio del producto se multiplica por la cantidad y se agrega a la variable "PrecioFactura"                
                        booleanito=False
                        input("Presione ENTER para continuar ")
                        system("cls")
                        condicional=False
                    else:
                        print("No se permiten cantidades negativas")
            else:
                print("Este ID no es de un producto existente, intente con otro")

    if r == 2:
        print(CarritoCompras)
        input("Presione ENTER para continuar ")
        system("cls")


    if r == 3:
        print ("El precio total de su compra es de",PrecioFactura,"$")
        input("Presione ENTER para continuar")
        system("cls")


    if r == 4:
        print("")
    
        print("Gracias por usar el programa, nos vemos luego :D")
        booleano=False
 
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470