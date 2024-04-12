booleano=True
while booleano==True: #Mientras sea verdadero repetir 
    print("=============BIENVENIDOOOOOOOOO===============") #Se muestra el menú y se muestran las posibles opciones que puede escoger el usuario
    print("""1). Ver el mínimo de monedas necesarias para cambiar un billete.
2). Mostrar un dato curioso.
3). Cerrar el programa.          
          """)
    opc = int(input("Ingrese el número de la opción que desea realizar: ")) #Se genera la entrada para que el usuario escoja la opción que quiera
    
    if opc==1: #Si la opción es 1, se muestra el proceso para calcular las monedas
        booleanito=True
        while booleanito==True: #Mientras sea verdadero hacer
            print(" ")
            booleanote=True 
            while booleanote==True: #Mientras sea verdadero hacer
                Monedas = [10,5,1] #Se crea una lista para meter los valores de las monedas que se tienen disponibles            
                Dinero = int(input("Por favor ingrese la cantidad de dinero que usted tiene: ")) #Se le pregunta la cantidad que desea pasar a monedas
                if Dinero>=1000: #Si ingresa un valor mayor a 1000 se le da el anuncio de que no es posible ejecutar el programa con este valor
                    print("Está sobrepasando el valor máximo, intente con uno menor a 1000")
                    booleanote=False #y booleanote pasa a ser falso, lo que hace que el programa se cierre
                else:                    
                    for i in Monedas: #Para i, hasta el rango de la lista monedas (que es tres), se va a recorrer la lista
                        if Dinero >= i: #Si el dinero que ingrese el usuario es mayor al valor de la moneda en el puesto i se va a hacer lo siguiente
                            CantidadMonedas = Dinero // i #La cantidad de monedas de i, va a ser la división con resultado entero del valor de la moneda en el puesto i entre la cantidad de dinero que se tenga
                            print("\nLa cantidad de monedas de:",i,"que neceitas es:", CantidadMonedas) #Se le muestra la cantidad de moneda de i, que se necesitan
                            Dinero = Dinero % i #El dinero va a pasar a ser el restante de la división entre el dinero y el valor de las monedas en el puesto i
                            contador = CantidadMonedas+CantidadMonedas #Contador que va a mostrar la cantidad de monedas que se entregaron en total
                    print("")
                    print("La cantidad de monedas que fueron entregadas es de: ",contador)
                    print("")
                    volver=str(input("¿Desea calcular otra cantidad? (SI/NO): ")) #Se le pregunta al usuario si desea calcular otro valor
                    if volver =="SI": #Si pone que sí, el proceso se repite
                        booleanito=True 
                    elif volver == "NO": #Si pone que no, el proceso se deja de ejecutar
                        booleanito=False
                        booleanote=False
                    else:
                        booleanito=False
                        booleanote=False
    if opc==2:
        print("Este programa me está dando dolor de cabeza") #Relleno
        print("")
        input("presione ENTER para continuar")
                
    else: #Si la opción que escoge el usuario es 2, el booleano pasa a ser falso y el programa se cierra
        booleano=False
#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470   