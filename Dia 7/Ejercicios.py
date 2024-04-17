print("Bienvenidos a nuestra tienda")
print("Este es nuestro catálogo")
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

booleano = True
while booleano==True:
    print(""""1. Agregar productos al carrito
    2. Ver el contenido del carrito
    3. Calcular el total de la compra
    4. Finalizar la compra
    5. Cerrar el programa      
        """)

    r = int(input("Escoja una de las opciones de nuestro menú"))
    if r == 1:
        print(productos)
    if r == 2:
        print("")
    if r == 3:
        print("")
    if r == 4:
        print("")
    if r == 5:
        booleano=False
