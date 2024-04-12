#Día #3

import string #Se importa la libreria de string, para usarla más adelante en el programa
import secrets #Se importa la libreria secrets, para que nos ayude a escoger caracteres aleatorios más adelante

booleano=True
while booleano==True: #Mientras sea verdadero hacer
    print("=============BIENVENIDO, CRACKKK=============") #Se le da la bienvenida al usuario al menú principal y se le muestran las opciones
    print("""1). Verificar si un número es primo o no.     
2). Para crear una contraseña que sea segura.
3). Cerrar el programa.
=============================================   
        """)
    opcion=int(input("\nEscribe el número de la opción que deseas realizar ")) #Se genera la entrada para que el usuario escoja 
    if opcion==1: #Dependiendo de lo que escoja el usuario se va a mandar a los diferentes subprocesos que se tienen en el programa
        booleanito=True #Con la opción "1" va a abrir el subprograma para los números primos
        while booleanito==True:
            print("") #Se le muestra al usuario las diferentes opciones que tiene escoger dentro de este subproceso
            print("=========================================")
            print("""1). Verificar un número.
2). Volver al inicio.
3). Información.
=========================================
""")
            r=int(input("Escribe el número de la opción que deseas realizar ")) #Se genera la entrada para que el usuario ponga su elección
            if r==1: #Dependiendo de lo que escoja se van a abrir los diferentes subprocesos que se tengan
                booleanito=True
                numero=int(input("\ningrese el número que desea verificar si es primo o no: ")) #Se le pregunta al usuario qué número desea verificar si es primo o no
                print(" ")                                                                      #y se le genera su respesctiva entrada
                cont=0 #Creamos un contador que empiece en cero
                for i in range(1,numero+1): #para i desde 1 hasta el número que ingrese el usuario+1 hacer
                        if numero % i == 0: #si el número que ingresó el usuario se divide con el número de la posición i y su residuo es 0
                            cont=cont+1 #se le va a sumar 1 al contador

                if cont==2: #si al finalizar el proceso, el contador está en 2 se da el anuncio de que el número, efectivamente es primo
                    print(numero,"Sí es un número primo") #ya que para ser primo solo debe ser divisible por él mismo y el 1
                else: #de lo contrario se le da el anuncio de que el número no es primo
                    print(numero,"No es un número primo")

            elif r==2: #Si escoge la opción 2 el booleano pasa a ser falso, lo que va a hacer que el subproceso se detenga
                booleanito=False
                
            else: #Si escoge la opción 3, se le da la información sobre los números primos y sobre la persona que creó este programa
                print("")
                print("""Los números primos son aquellos que solo son divisibles por ellos mismos.
Si se intenta dividir por otro número nunca dará una cifra exacta salvo que se divida por 1 o por sí mismo.
                      
Programa desarrollado por Brayan Maldonado
Edad: 16 años
Municipio: Tibú, Norte de Santander
Fecha: 11/04/23
""")
    
    elif opcion==2: #Si en el menú principal, el usuario escoge la opción 2, se abre el programa de las contraseñas seguras
        booleanito2=True
        while booleanito2==True: #Mientras sea verdadero hacer
            #Se les da valor a algunas variables con la libreria string, para que nos den valores de texto
            LetrasMa = string.ascii_uppercase #Variable de las mayúsculas   
            LetrasMi = string.ascii_lowercase #Variable de las minusculas
            Digitos = string.digits #Variable de los números (como string)
            CaracEspe = string.punctuation #Variable de los carácteres especiales

            Alfabeto = LetrasMa+LetrasMi+Digitos+CaracEspe #Se va a crear una variable en la que se incluyan todos los valores que se guardaron en las variables anteriores
            print("PROGRAMA DE CONTRASEÑAS") #Se le da la bienvenida al usuario y se le muestran las opciones
            print("""1). Crear una contraseña segura 
2). Volver al menú principal
""")
            print("")
            opc=int(input("Elija el número de la opción que desea realizar ")) #Se genera la entrada para que ingrese su elección
            print("")
            if opc==1: #Si la opción es "1" se le hacen las preguntas para crear la contraseña segura según lo que escoja el usuario
                LlevaN = str(input("Desea que su contraseña contenga números? (SI/NO) "))
                print("")
                LlevaEsp = str(input("Desea que su contraseña contenga caracteres especiales? (SI/NO) "))
                print("")
                LlevaM = str(input("Desea que su contraseña contenga letras mayúsculas? (SI/NO) "))
                print("")
                if LlevaM=="SI": #Serie de pasos para que en la variable "Alfabeto" queden los valores que escogió el usuario
                   Alfabeto=LetrasMi+Digitos+CaracEspe 
                   if LlevaN=="NO":
                        Alfabeto=LetrasMi+CaracEspe
                        if LlevaEsp=="NO":
                             Alfabeto=LetrasMi
                   if LlevaN=="SI":
                        Alfabeto=LetrasMi+Digitos
                        if LlevaEsp=="SI":
                             Alfabeto=LetrasMi+CaracEspe
                             
                if LlevaN=="NO":
                    Alfabeto=LetrasMa+Digitos+CaracEspe
                    if LlevaN=="NO":
                            Alfabeto=LetrasMa+CaracEspe
                            if LlevaEsp=="NO":
                                Alfabeto=LetrasMa

                Tamaño=int(input("¿Cuántos caracteres desea que tenga su contraseña? ")) #Se le pregunta al usuario cuántos carácteres desea que tenga su contraseña segura
                print("")
                Enter=input("Presione ENTER para ver su contraseña") #Se espera de una tecla para que no se muestre el resultado de una vez, para que sea vea más estético
                Pass="" #se crea la variable "pass", en la cual se va a guardar la contraseña
                for i in range(1,Tamaño+1): #para i desde 1 hasta el tamaño que diga el usuario+1
                     Pass += "".join(secrets.choice(Alfabeto))  #A la varibale "pass" se le va a ir agregando un caracter al azar que esté dentro de la variable "abecedario"
                
                if i==Tamaño: #Cuando el contador alcance el valor que escogió el usuario se va a mostrar la contraseña
                     print(Pass)

            else: #Si escoge la opción 2 u otra diferente el booleano pasa a ser falso, lo que va a hacer que el programa se cierre
                booleanito2=False

    else:
        print("NOS VEMOS LUEGOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO") #Despedida del programa
        break
    ##Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470