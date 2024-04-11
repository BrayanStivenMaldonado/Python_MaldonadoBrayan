booleanito=True
while booleanito==True:
    print("")
print("""1). Verificar un número
        2). Detener el programa
        3). Información adicional
        """)
r=input()
if r==1:
        numero=int(input("INGRESE EL NÚMERO QUE DESEA VERIFICAR PARA SABER SI ES PRIMO O NO"))
        cont=0
        for i in range(0,numero):
            if numero%i==0:
                cont=cont+1
        if cont==2:
            print(numero,"No es un número primo")
        else:
            print(numero,"No es un número primo")
if r==2:
   booleanito=False