#Llamamos a la libreria system para luego usar la opción de limpiar pantalla ("cls")
from os import system

import json

#Llamado del archivo Json para poder usarlo dentro del programa
with open('Dia 11/Brayan.json', encoding='utf-8') as f:
    datos = json.load(f)

#Conjuntos en los que van a ir guardados algunos valores para posteriormente imprimirlos cuando se requiera
TodosID = []
TodosEventos = []
Evento = []

booleano =True #Definimos como "True" un booleano para usarlo como condicional del "while"

while booleano == True: #Cada vez que salga de una opción vuelve al menú de opciones

    for i in range (len(datos)): #Guardar todos los eventos en una lista separada
        TodosEventos.append(datos[i]["type"])

    for i in range (len(datos)): #Guardar todos los id's en una lista separada
        TodosID.append(datos[i]["id"])

    for i in range (len(datos)): #Guardar los nombres de los eventos sin repetir en una lista separada
        if datos[i]["type"] not in Evento:
            Evento.append(datos[i]["type"])

    print("""
    ------MENU DE OPCIONES------
    1). Revisar
    2). Crear
    3). Actualizar
    4). Eliminar
    5). Cerrar programa
        """)

    eleccion = int(input("Ingrese su elección: ")) #Dependiendo de lo que escoja el usuario se van a mostrar las diferentes opciones
    system("cls")

    if eleccion == 1:
        print("------------------EVENTOS------------------")

        for i in range (len(Evento)): #Mostrar los nombres de los eventos que hay dentro de la mini-base de datos
            print(i+1,":",Evento[i])

        print("------------------------------------------------")
        EventoVer = input("Ingrese el nombre de los eventos que desea revisar: ") #Se le pide al usuario que ingrese el nombre de los eventos que desea revisar
        print("------------------------------------------------")
        for i in range (len(TodosEventos)):
            if EventoVer == (TodosEventos[i]): #Se imprimen todos los valores que sean del tipo de evento que escogió el usuario
                print("Evento #",i+1, ":",TodosEventos[i],"---","id: ",TodosID[i])         
            
        if EventoVer not in TodosEventos: #Si el nombre del tipo de evento que ingresa el usuario no existe, se le da el anuncio
            print("Este tipo de evento no existe dentro de la base de datos, por favor ingrese uno de los de la lista")

        print("")
        input("Presione ENTER para continuar") #Se limpia la consola, para que se vea más ordenado
        system("cls")


    elif eleccion ==2:
        print("------------------CREAR------------------")
        print("")
        EventoAgregar = str(input("Ingrese el nombre del evento que desea agregar: ")) #Se pide que ingrese el nombre del evento que va a agregar y se guarda en una variable
        print("----------------------------------------------")
        IdAgregar = int(input("Ingrese el ID del evento que desea agregar: ")) #Se pide que ingrese el id del evento que desea va a agregar y se guarda en una variable
        nuevo = {"type": EventoAgregar, "id": IdAgregar} #Se genera otra variable la cual va a guardar un subdiccionario que va a guardar los valores de las dos variables que anteriormente creamos
        datos.append(nuevo) #La variable que guardó los valores del diccionario se agrega al archivo
        print("")
        print("El evento (",EventoAgregar,") ha sido añadido con éxito!") #Se anuncia de que se ha añadido su evento
        print("")
        input("Presione ENTER para continuar")
        system("cls")

    elif eleccion == 3:
        print("------------------ACTUALIZAR------------------")
        print("")
        IdActualizar = int(input("Ingrese el ID del evento que desea actualizar: ")) #Se le pide que ingrese el id del evento que desea eliminar
        for i in datos:
            if i["id"] == IdActualizar: #Si el id que ingresa sí existe
                EventoActualizar = str(input("Ingrese el nuevo tipo de evento: ")) #Se le pide que ingrese el nuevo nombre que le desea poner al evento
                i["type"] = EventoActualizar #El evento ("type") en la posición que se encontró que era igual al id que puso el usuario va a pasar a ser lo que ingresó anteriormente
                print("")
                print("Evento actualizado! ") #Se le dice que su evento fue actualizado
        
        if i["id"] != IdActualizar: #Si el id que ingresa no existe se le da el anuncio de que intente con otro
            print("Lo siento, este ID no existe, intente con otro")
        
        print("")
        input("Presione ENTER para continuar")
        system("cls")

    elif eleccion == 4:
        print("------------------ELIMINAR------------------")
        print("")
        Eliminar = int(input("Ingrese el ID del evento que desea eliminar: ")) #Se le pide que ingrese el id del evento que desea eliminar
        for i in datos: 
            if i["id"] == Eliminar: #Si el id que ingresa está dentro de los datos
                datos.remove(i) #se remueve el elemento que está en la posición que se encontró que era igual
                print("")
                print("Evento eliminado!")

        if i["id"] != Eliminar: #Si el id que ingresa no existe se le da el anuncio de que debe intentarlo con otro
            print("Lo siento, este ID no existe, intente con otro")

        print("")
        input("Presione ENTER para continuar")
        system("cls")

    else: #Si ingresa una opción diferente a las cuatro que ya están definidas el programa se cerrará
        booleano = False
        print("Está saliendo del programa")
        print("")
        input("Presione ENTER para continuar")
        system("cls")

#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470