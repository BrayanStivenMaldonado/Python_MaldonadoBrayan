#Diccionario system para usar el comando "cls"
from os import system

#Tupla en la que se guardan los valores de las frutas que hay en stock
Fruits=[("Banana",0.45,6),("Kiwi",4.55,5),("Sandia",5,2)]

#Menu para que el usuario escoja lo que desea visualizar en pantalla
booleanito = True
while booleanito == True:

    print("""
    =====MENU DE LA FRUTERIA DE PYTIMES=====
    1). Mostrar las frutas que hay en stock
    2). Mostrar las frutas que tienen un precio menor a 0.50
    3). Mostrar la fruta con más cantidad en stock
    4). Mostrar el precio de todas las frutas que hay en stock
    5). Cerrar el programa
        """)
    print("")
    eleccion = int(input("Ingrese el número de la acción que desea realizar: ")) #se le genera la entrada para que ingrese la eleccion
    system("cls")

    if eleccion == 1: 
            print("===STOCK===") #Se muestran las frutas que se tienen en stock
            for i in Fruits:print(i[0])
            print("")
            input("Presione ENTER para continuar")
            system("cls")


    if eleccion == 2:
            print("FRUTAS CON PRECIO MENOR A 0.50") #Se muestran las frutas que tienen un precio menor a 0.50
            for i in Fruits: 
                if i[1] <= 0.50:
                    print(i)
            print("")
            input("Presione ENTER para continuar")
            system("cls")

    if eleccion == 3:
            print("FRUTA CON MÁS CANTIDAD EN STOCK") #Se muestra la fruta de la que más unidades en stock se tienen
            FrutaMayor=max(Fruits, key=lambda x: x[2]); print(FrutaMayor)
            print("")
            input("Presione ENTER para continuar")
            system("cls")

    if eleccion == 4:
            print("PRECIO DE LA FRUTA MULTIPLICADO CON SU CANTIDAD EN STOCK") #Se multiplica el precio de la fruta por la cantidad de unidades que se tienen en stock
            for i in Fruits:
                Precio=i[1]*i[2]
            print(Precio)
            print("")
            input("Presione ENTER para continuar")
            system("cls")

    if eleccion ==5:
            print("Gracias por preferir a la fruteria de PYTimes, nos vemos luego :D")
            booleanito=False
        
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470