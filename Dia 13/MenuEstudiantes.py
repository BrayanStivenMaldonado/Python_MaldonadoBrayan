from os import system #Libreria system para usar la opción "cls"

#Libreria para poder usar los archivos .json
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
          
    #Para que no pueda ingresar un número diferente a los que se tienen dentro de el .json
    booleanoEleccion = True    
    #Booleano para la elección del grupo que el usuario va a editar
    while booleanoEleccion == True:
        print("""
Grupos dentro de la base de datos: 
1. T2
2. P1          
          """)        
        GrupoEleccion = int(input("¿Qué grupo desea editar?: ")) #Se le pregunta a cuál grupo desea editar 
        
        if GrupoEleccion==1 or GrupoEleccion==2: #Si es alguno de los dos grupos posibles el programa continua
            booleanoEleccion=False
            GrupoEleccion = GrupoEleccion-1 #Se le resta 1 a la opción ya que los valores de los indices empiezan desde "0" y no desde "1"
            system("cls")
            
        elif GrupoEleccion!=1 or GrupoEleccion!=2: #Si no es ninguno de los grupos disponibles se le vuelve a preguntar el número hasta que escoja alguno de los posibles
            print("")
            print("Solo hay 2 grupos, intente de nuevo")
            input("Presione ENTER para continuar")
            system("cls")
    
    #Menú en el que se muestran las opciones posibles
    print("MENU DE OPCIONES")
    print("\n1. Revisar estudiantes\n2. Modificar estudiante\n3. Crear Estudiante\n4. Eliminar Estudiante\n5. Cerrar Programa\n")
    Eleccion = int(input("¿A qué grupo deseas ingresar?: "))
    system("cls")
    
    GeneralData=[]

    #Revisar estudiantes
    if(Eleccion==1):
        GeneralData=abrirArchivo()
        contador=0
        for i in GeneralData[GrupoEleccion]["estudiantes"]: #Se muestran los estudiantes dentro de la sublista 0, donde están Jerxon y Wilmer
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
            
        input("Presiona ENTER para continuar")
        system("cls")

    #Modificar algún estudiante
    elif(Eleccion==2):
        GeneralData=abrirArchivo()
        contador = 0
        for i in GeneralData[GrupoEleccion]["estudiantes"]:
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
        
        estudiante = int(input("Cual Numero de estudiante vas a cambiar? "))
        datoCambiar=int(input("Que te gustaría cambiar del estudiante:\n1.Apellido:\n2.Nombre:\n3.Edad:\n4.Fecha de Nacimiento:\n5.Cedula:\n6.E-mail\n7.Github\n"))
        if (datoCambiar==1):
            nuevoApellido = input("Ingresa el nuevo apellido: ")
            GeneralData[GrupoEleccion]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            
        elif (datoCambiar==2):
            nuevoNombre = input("Ingresa el nuevo Nombre: ")
            GeneralData[GrupoEleccion]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            
        elif (datoCambiar==3):
            nuevaEdad = int(input("Ingresa la nueva edad: "))
            GeneralData[GrupoEleccion]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            
        elif (datoCambiar==4):
            nuevaFechaNac = input("Ingresa la nueva Fecha de Nacimiento: ")
            GeneralData[GrupoEleccion]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevaFechaNac
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            
        elif (datoCambiar==5):
            nuevaCedula = int(input("Ingresa la nueva Cedula: "))
            GeneralData[GrupoEleccion]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            
        elif (datoCambiar==6):
            nuevoEmail = input("Ingresa el nuevo E-mail: ")
            GeneralData[GrupoEleccion]["estudiantes"][estudiante-1]["email"] = nuevoEmail
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            
        elif (datoCambiar==7):
            nuevoGitHub = input("Ingresa el nuevo GitHub: ")
            GeneralData[GrupoEleccion]["estudiantes"][estudiante-1]["github"] = nuevoGitHub
            guardarArchivo(GeneralData)
            print("Cambio Guardado con éxito!")
            
        contador = 0
        GeneralData=abrirArchivo()
        for i in GeneralData[GrupoEleccion]["estudiantes"]:
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
        
        print("")
        input("Presione ENTER para continuar")
        system("cls")

    #Crear estudiante
    elif (Eleccion==3):
        GeneralData=abrirArchivo()
        id_estu = int(input("Ingresa el ID del nuevo estudiante: "))
        for i in GeneralData[GrupoEleccion]["estudiantes"]:
            if GeneralData[GrupoEleccion]["id"] == id_estu:
                print("Este ID de estudiante ya existe!")
                break
            
            elif GeneralData[GrupoEleccion]["id"] != id_estu:
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese Apellido: ")
                edad = int(input("Ingrese Edad: "))
                fechaNac = input("Ingrese fecha de Nacimiento (DD-MM-AAAA): ")
                cedula = int(input("Ingrese Numero de Cedula: "))
                email = input("Ingrese E-mail: ")
                github = input("Ingrese Github: ")
                GeneralData[GrupoEleccion]["estudiantes"].append({
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
                print("Creado Exitosamente!")
                break
        
        input("Presione ENTER para continuar")
        system("cls")    
                
    #Eliminar estudiante                 
    elif (Eleccion==4):
        x=0
        GeneralData=abrirArchivo()
        
        for i in GeneralData[GrupoEleccion]["estudiantes"]:
            print("===========================")
            print("ESTUDIANTE #",x+1)
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
            x = x + 1
            
        Estudianteeliminar = int(input("Ingrese el # del alumno a eliminar: "))
        Estudianteeliminar = Estudianteeliminar-1
        
        del GeneralData[GrupoEleccion]["estudiantes"][Estudianteeliminar]            
        guardarArchivo(GeneralData)
        print("Eliminado exitosamente!") 
        input("Presione ENTER para continuar")
        system("cls")       

    #Cerrar programa
    elif (Eleccion==5): 
        print("Programa Cerrado!")
        booleano = False

    #Opción no válida
    else:
        print("Esta no es una opción válida, intente de nuevo: ")
        input("Presione ENTER para continuar")
        system("cls")

#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470