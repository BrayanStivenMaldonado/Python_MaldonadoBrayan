#--------------------------------#
#----DIA 1 CHEAT SHEET PYTHON----#
#--------------------------------#

#imprimir hola mundo
print("Hola mundoooooo!")

#Datos primitivos 

#Numero
Numerito = 1 #Nombre variable = valor
print(Numerito) #Imprimir (variable)
print(type(Numerito)) #Imprimir (tipo(variable))

#Decimal
NumeroDecimal = 1.1
print(NumeroDecimal)
print(type(NumeroDecimal))

#Booleano
MiBooleanito = True
print(MiBooleanito)
print(type(MiBooleanito))

#CadenaDeTexto
Texto = "Queloque"
print(Texto)
print(type(Texto))
 
 #TALLER
 
#Ingresar información por teclado
Informacion = input("Ingrese un dato ")
print("El dato ingresado es:",Informacion)

#Conversion de tipos de variable (tipos de datos primitivos)
print(int(8))
print(float(8,5))
print(str("Ocho"))
print(bool(True))
print(bool(False))

#Bucles For y While
#For
nc= int(input("Ingrese el numero maximo"))
for i in range(1,(1+nc)):
    print ("numeros",i)

#While
numero = 1
while numero <= 10:
    print(numero)
    numero +=1
print("Proceso terminado")
#Funciones (4 tipos)
print("Funciones")

#Funcion 1
print("Funcion 1")
def nose():
    print(2+4)

#Funcion 2
print("Funcion 2")
def saludo():
    print("Hola crackk")

#Funcion 3
print("Funcion3")
def SaludaNombre(nombre):
    print("Hola",nombre,"feliz dia")

#Funcion 4
print("Funcion 4")
def multiplicacion(n,m):
    return(n*m)

#Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470