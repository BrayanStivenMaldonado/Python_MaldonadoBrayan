from os import system #Libreria system para usar la opción "cls"

import json

def abrirArchivo(): #Función que va a servir para abrir el archivo
    miJSON=[]
    with open('Dia 13/info.json','r',encoding='utf-8') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData): #Función que va a servir para guardar los datos que se realicen al archivo
    with open("Dia 13/info.json","w",encoding='utf-8') as outfile:
        json.dump(miData,outfile)

booleano = True #Booleano para usarlo como condición del while
while booleano == True: #While para que cada vez que salga de alguna opción vuelva al menú principal

    print("===========================") #Menú en el que se muestran las opciones posibles
    print("  MENU DE OPCIONES")
    print("===========================")
    print("Por favor escoge alguna de las siguientes opciones:\n \n1.Revisar estudiantes\n2.Modificar estudiante\n3.Crear Estudiante\n4.Eliminar Estudiante\n5. Cerrar Programa\n")
    Eleccion = int(input("¿Qué deseas hacer?: "))
    system("cls")
    GeneralData=[]

    #Revisar estudiantes
    if(Eleccion==1):
        GeneralData=abrirArchivo()
        contador=0
        for i in GeneralData[0]["estudiantes"]: #Se muestran los estudiantes dentro de la sublista 0, donde están Jerxon y Wilmer
            contador = contador +1
            print("===========================")
            print(" ESTUDIANTE #",contador)
            print("ID:",i["id"])
            print("Nombre:",i["nombre"])
            print("Apellido:",i["apellido"])
            print("Edad",i["edad"])
            print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
            print("Cédula:",i["cedula"])
            print("E-mail:",i["email"])
            print("GitHub:",i["github"])
            print("===========================")
            print("")

    #Modificar algún estudiante
    elif(Eleccion==2):
        GeneralData=abrirArchivo()
        contador = 0
        for i in GeneralData[0]["estudiantes"]:
            contador = contador +1
            print("===========================")
            print(" ESTUDIANTE #",contador)
            print("ID:",i["id"])
            print("Nombre:",i["nombre"])
            print("Apellido:",i["apellido"])
            print("Edad",i["edad"])
            print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
            print("Cédula:",i["cedula"])
            print("E-mail:",i["email"])
            print("GitHub:",i["github"])
            print("===========================")
            print("")
        contador = 0
        estudiante = int(input("Cual Numero de estudiante vas a cambiar? "))
        datoCambiar=int(input("Que te gustaría cambiar del estudiante:\n1.Apellido:\n2.Nombre:\n3.Edad:\n4.Fecha de Nacimiento:\n5.Cedula:\n6.E-mail\n7.Github\n"))
        if (datoCambiar==1):
            nuevoApellido = input("Ingresa el nuevo apellido: ")
            GeneralData[0]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            contador = 0
        elif (datoCambiar==2):
            nuevoNombre = input("Ingresa el nuevo Nombre: ")
            GeneralData[0]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            contador = 0
        elif (datoCambiar==3):
            nuevaEdad = int(input("Ingresa la nueva edad: "))
            GeneralData[0]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            contador = 0
        elif (datoCambiar==4):
            nuevaFechaNac = input("Ingresa la nueva Fecha de Nacimiento: ")
            GeneralData[0]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevaFechaNac
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            contador = 0
        elif (datoCambiar==5):
            nuevaCedula = int(input("Ingresa la nueva Cedula: "))
            GeneralData[0]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            contador = 0
        elif (datoCambiar==6):
            nuevoEmail = input("Ingresa el nuevo E-mail: ")
            GeneralData[0]["estudiantes"][estudiante-1]["email"] = nuevoEmail
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            contador = 0
        elif (datoCambiar==7):
            nuevoGitHub = input("Ingresa el nuevo GitHub: ")
            GeneralData[0]["estudiantes"][estudiante-1]["github"] = nuevoGitHub
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            contador = 0
        GeneralData=abrirArchivo()
        for i in GeneralData[0]["estudiantes"]:
            contador = contador +1
            print("===========================")
            print(" ESTUDIANTE #",contador)
            print("ID:",i["id"])
            print("Nombre:",i["nombre"])
            print("Apellido:",i["apellido"])
            print("Edad",i["edad"])
            print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
            print("Cédula:",i["cedula"])
            print("E-mail:",i["email"])
            print("GitHub:",i["github"])
            print("===========================")
            print("")
        contador = 0

    #Crear un nuevo estudiante
    elif (Eleccion==3):
        GeneralData=abrirArchivo()
        id_estu = int(input("Ingresa el ID del nuevo estudiante: "))
        for i in GeneralData[0]["estudiantes"]:
            if id_estu == GeneralData[0]["id"]:
                print("ID ya eEleccioniste")
                break
            
            else:
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese Apellido: ")
                edad = int(input("Ingrese Edad: "))
                fechaNac = input("Ingrese fecha de Nacimiento (DD-MM-AAAA): ")
                cedula = int(input("Ingrese Numero de Cedula: "))
                email = input("Ingrese E-mail: ")
                github = input("Ingrese Github: ")
                GeneralData[0]["estudiantes"].append({
                "id": id_estu,
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "fechaNacimiento": fechaNac,
                "cedula": cedula,
                "email": email,
                "github": github
                })
                guardarArchivo(GeneralData)
                print("Estudiante Creado con eEleccionito!!!")
                break
                                 
    elif (Eleccion==4):
        a=0
        GeneralData=abrirArchivo()
        
        for i in GeneralData[0]["estudiantes"]:
            print("===========================")
            print("ESTUDIANTE #",a+1)
            print("ID:",i["id"])
            print("Nombre:",i["nombre"])
            print("Apellido:",i["apellido"])
            print("Edad",i["edad"])
            print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
            print("Cédula:",i["cedula"])
            print("E-mail:",i["email"])
            print("GitHub:",i["github"])
            print("===========================")
            print("")
            a = a + 1
        eliminar = int(input("Ingrese el ID del alumno a eliminar: "))

        del GeneralData[0]["estudiantes"][eliminar]
        guardarArchivo(GeneralData)
        print("eliminado con eEleccionito")

    elif (Eleccion==5): 
        print("Programa Cerrado")
        booleano = False

    else:
        print("Esta no es una opción válida, intente de nuevo: ")
        input("Presione ENTER para continuar")
        system("cls")

#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470