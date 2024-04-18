#Llamamos a la libreria system para luego usar la opción de limpiar pantalla ("cls")
from os import system

#Se define el precio que va a tener la suscripción al periodico
PrecioDeSuscripcion = 50000

#Conjunto en el que se van a guardar los datos de los usuarios
Usuarios = [""]

#Conjunto en el que se van a guardar los datos de las contraseñas
Contraseñas = [""]

#Dinero del cliente 
DineroCliente = 0

#Inicio del programa
booleanito = True
while booleanito == True: #Se crea el while junto con un booleano para que cada vez que el usuario salga de una opcion se vuelva al menú principal
    
    print("""
    =============MENU DE OPCIONES============= 
    1). Iniciar sesión
    2). Comprar una suscripcion a PYTimes
    3). Recargar tu cuenta
    4). Cerrar el programa 
        """)
    eleccion = int(input("Escoja el número de la opción que desea realizar: ")) #Se le muestra el menú de opciones y se le da la entrada para que escoja la que desea realizar

    if eleccion == 1: #Si la elección en "1" se da inicio al proceso de inicio de sesión
        print("===Iniciar Sesión===")
        IngresoUsuario = input("Ingrese su nombre de usuario: ") #Se le pide que ingrese el nombre su nombre de Usuario
        if IngresoUsuario in Usuarios: #Si el nombre que ingrese el Usuario está dentro de la lista de "Usuarios" se le va a pedir que ingrese la contraseña de la cuenta
            IngresoContraseña = input("Ingrese su contraseña ") 
            if IngresoContraseña in Contraseñas: #Si la contraseña que ingrese está dentro de la lista "Contraseñas" se le da acceso a las noticias
                    print("""
                          Has ingresado con éxito
                          Aqui
                          Va
                          Contenido
                          """)
                    input("Presione ENTER para continuar")
            else: 
                    print("Contraseña incorrecta") #Si la contraseña que ingrese no está dentro de la lista "Contraseñas" se le da el anuncio de que ha ingresado una contraseña incorrecta          
        else:
            print("Usuario incorrecto") #Si el nombre de usuario que ingrese no está dentro de la lista "Usuarios" se le da el anuncio de que ha ingresado un nombre de usuario incorrecto           
            input("Presione ENTER para continuar ")
            system("cls")
        
    elif eleccion ==2: #Si la elección en "2" se da inicio al proceso de la compra de la suscripción
        print("===Comprar una suscripcion===")
        print("Su dinero en la cuenta es de: ",DineroCliente) #Se le muestra al usuario el dinero que tiene en la cuenta
        if DineroCliente >= PrecioDeSuscripcion: #Si el dinero que tiene en la cuenta es mayor al precio de la suscripción se le permite que continue el proceso
            SiNo = str(input("¿Desea comprar una suscripción? (SI/NO) ")) #Se le pregunta si desea comprar una suscripcion y se crea la entrada para que ponga su elección
            if SiNo == "SI":
                AÑosComprar = int(input(" Cuántos años de acceso al periodico desea adquirir? ")) #Se le pregunta cuántos años de suscripción desea comprar
                if PrecioDeSuscripcion*AÑosComprar>DineroCliente: #Si el resultado del precio total de los años que desea comprar es mayor al dinero que tiene el cliente 
                    print("No tienes suficiente dinero, recuerda que la suscripción anual tiene un costo de: ",PrecioDeSuscripcion) #se le da el anuncio de que no le alcanza el dinero para comprar esa cantidad de años de suscripción
                else:
                    CantidadAños = int(input("Desde qué año desea que empiece a cubrir su suscripción ")) #Se le pregunta desde qué año desea que empiece a cubrir su suscripción
                    if CantidadAños>= 2023: #El año que ingrese tiene que ser mayor o igual a 2023 (porque ese es el año en el que estamos)
                        Usuarios.append(str(input("Ingrese su nombre de usuario: "))) #Si cumple todas las condiciones anteriores se le va a pedir que ingrese el Usuario 
                        Contraseñas.append(str(input("Ingrese su contraseña ")))       #Y la contraseña de la cuenta que va a adquirir
                        AcabaSuscripcion = AÑosComprar+CantidadAños
                        DineroCliente-=PrecioDeSuscripcion*AÑosComprar #Al dinero del cliente se le va a restar lo que costó la suscripción que acaba de adquirir
                        print("Su sucripción se va a acabar el año",AcabaSuscripcion) #El año en el que se le va a acabar la suscripción va a ser la suma del año de inicio y la cantidad de años que va a adquirir
                        print("")
                        print("Su saldo actual ahora es de:", DineroCliente)
                    else:
                        print("No puedes escoger un año de inicio que ya haya pasado") #Si pone un año menor se le da el anuncio de que no puede escoger un año que ya haya pasado
            else:
                print("ok :D")              
        else:
            print("Lo siento, no tienes suficiente dinero en la cuenta :c") #Si no tiene suficiente dinero en la cuenta para comprar por lo menos un año de suscripción se le da el anuncio de que no tiene suficiente dinero
            print("Saldo actual:",DineroCliente) #Se le muestra el dinero que tiene en la cuenta
               
        if DineroCliente>= PrecioDeSuscripcion:
            SiNoRegalo = str(input("¿Desea regalarle una suscripción a algún amigo? (SI/NO)"))
            if SiNoRegalo == "SI":
                AÑosComprar = int(input(" Cuántos años de acceso al periodico desea adquirir? ")) #Se le pregunta cuántos años de suscripción desea comprar
                if PrecioDeSuscripcion*AÑosComprar>DineroCliente: #Si el resultado del precio total de los años que desea comprar es mayor al dinero que tiene el cliente 
                    print("No tienes suficiente dinero, recuerda que la suscripción anual tiene un costo de: ",PrecioDeSuscripcion) #se le da el anuncio de que no le alcanza el dinero para comprar esa cantidad de años de suscripción
                else:
                    CantidadAñosRegalo = int(input("Desde qué año desea que empiece a cubrir su suscripción ")) #Se le pregunta desde qué año desea que empiece a cubrir su suscripción
                    if CantidadAñosRegalo>= 2023: #El año que ingrese tiene que ser mayor o igual a 2023 (porque ese es el año en el que estamos)
                        Usuarios.append(str(input("Ingrese el nombre de usuario de la cuenta que desea regalar: "))) #Si cumple todas las condiciones anteriores se le va a pedir que ingrese el Usuario 
                        Contraseñas.append(str(input("Ingrese la contraseña de la cuenta que desea regalar: ")))       #Y la contraseña de la cuenta que va a adquirir
                        AcabaSuscripcion = AÑosComprar+CantidadAños
                        DineroCliente-=PrecioDeSuscripcion*AÑosComprar #Al dinero del cliente se le va a restar lo que costó la suscripción que acaba de adquirir
                        print("La suscripción de la cuenta que va a regalar se va a acabar el año",AcabaSuscripcion) #El año en el que se le va a acabar la suscripción va a ser la suma del año de inicio y la cantidad de años que va a adquirir
                        print("")
                        print("Su saldo actual ahora es de:", DineroCliente)
                    else:
                        print("No puedes escoger un año de inicio que ya haya pasado") #Si pone un año menor se le da el anuncio de que no puede escoger un año que ya haya pasado              
                
               
        input("Presione ENTER para continuar ")
        system("cls")
        
    elif eleccion ==3:
        print("Recargar tu cuenta")
        DineroAñadir = int(input("¿Cuánto dinero desea añadir a su cuenta? ")) #Se le pregunta cuánto dinero desea añadir a la cuenta
        DineroCliente += DineroAñadir #Ahora el dinero del cliente va a ser lo que tenía sumado con lo que va a añadir
        print("Su dinero fue añadido a la cuenta exitosamente")
        input("Presione ENTER para continuar ")
        system("cls")
        
    else:
        print("Gracias por preferir PYTimes, nos vemos luego :D")
        booleanito = False
        
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470