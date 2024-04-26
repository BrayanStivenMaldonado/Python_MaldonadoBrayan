from os import system

import json

def abrirArchivo():
    miJSON=[]
    with open('Dia 13/info.json','r',encoding='utf-8') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("Dia 13/info.json","w",encoding='utf-8') as outfile:
        json.dump(miData,outfile)

booleano = True
while booleano == True:

    print("===========================")
    print("  MENU DE OPCIONES")
    print("===========================")
    print("Por favor escoge alguna de las siguientes opciones:\n \n1.Revisar estudiantes\n2.Modificar estudiante\n3.Crear Estudiante\n4.Eliminar Estudiante\n5. Cerrar Programa\n")
    Eleccion = int(input("¿Qué deseas hacer?: "))
    system("cls")
    miInfo=[]

    #Revisar estudiantes
    if(Eleccion==1):
        miInfo=abrirArchivo()
        contador=0
        for i in miInfo[1]["estudiantes"]:
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
        miInfo=abrirArchivo()
        contador = 0
        for i in miInfo[1]["estudiantes"]:
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
            miInfo[1]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
            guardarArchivo(miInfo)
            print("Cambio Guardado!")
            contador = 0
        elif (datoCambiar==2):
            nuevoNombre = input("Ingresa el nuevo Nombre: ")
            miInfo[1]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
            guardarArchivo(miInfo)
            print("Cambio Guardado!")
            contador = 0
        elif (datoCambiar==3):
            nuevaEdad = int(input("Ingresa la nueva edad: "))
            miInfo[1]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
            guardarArchivo(miInfo)
            print("Cambio Guardado!")
            contador = 0
        elif (datoCambiar==4):
            nuevaFechaNac = input("Ingresa la nueva Fecha de Nacimiento: ")
            miInfo[0]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevaFechaNac
            guardarArchivo(miInfo)
            print("Cambio Guardado!")
            contador = 0
        elif (datoCambiar==5):
            nuevaCedula = int(input("Ingresa la nueva Cedula: "))
            miInfo[1]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
            guardarArchivo(miInfo)
            print("Cambio Guardado!")
            contador = 0
        elif (datoCambiar==6):
            nuevoEmail = input("Ingresa el nuevo E-mail: ")
            miInfo[1]["estudiantes"][estudiante-1]["email"] = nuevoEmail
            guardarArchivo(miInfo)
            print("Cambio Guardado!")
            contador = 0
        elif (datoCambiar==7):
            nuevoGitHub = input("Ingresa el nuevo GitHub: ")
            miInfo[1]["estudiantes"][estudiante-1]["github"] = nuevoGitHub
            guardarArchivo(miInfo)
            print("Cambio Guardado!")
            contador = 0
        miInfo=abrirArchivo()
        for i in miInfo[1]["estudiantes"]:
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
        miInfo=abrirArchivo()
        id_estu = int(input("Ingresa el ID del nuevo estudiante: "))
        for i in miInfo[1]["estudiantes"]:
            if id_estu == miInfo[1]["id"]:
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
                miInfo[1]["estudiantes"].append({
                "id": id_estu,
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "fechaNacimiento": fechaNac,
                "cedula": cedula,
                "email": email,
                "github": github
                })
                guardarArchivo(miInfo)
                print("Estudiante Creado con eEleccionito!!!")
                break
                                 
    elif (Eleccion==4):
        a=0
        miInfo=abrirArchivo()
        
        for i in miInfo[1]["estudiantes"]:
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

        del miInfo[1]["estudiantes"][eliminar]
        guardarArchivo(miInfo)
        print("eliminado con eEleccionito")

    elif (Eleccion==5): 
        print("Programa Cerrado")
        booleano = False

    else:
        print("Esta no es una opción válida, intente de nuevo: ")
        input("Presione ENTER para continuar")
        system("cls")

#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470

