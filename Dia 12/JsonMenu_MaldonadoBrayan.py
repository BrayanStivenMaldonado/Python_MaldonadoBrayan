#Se importa la libreria "system" para usar la opción ("cls")
from os import system

#importamos la libreria json para poder importar el archivo.json
import json

#Importamos el archivo Json para usarlo dentro del código
with open ('Dia 12/Brayan.json',encoding='utf-8') as openfile:
    DatosGeneral = json.load(openfile)

#Listas en las que se van a guardar los valores de los diferentes eventos que hay   
TodosLosEventos = []
CreateEvent = []
PushEvent = []
WatchEvent = []
ReleaseEvent = []
PullRequestEvent = []
IssuesEvent = []
ForkEvent = []
GollumEvent = []
IssueCommentEvent = []
DeleteEvent = []
PullRequestReviewCommentEvent = []
CommitCommentEvent = []
MemberEvent = []
PublicEvent = []

#Serie de ciclos for que van a servir para agregar los diferentes eventos, junto con sus valores a las respectivas listas
for i in range (len(DatosGeneral)):
    TodosLosEventos.append(DatosGeneral[i])

for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "CreateEvent":
        CreateEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "PushEvent":
        PushEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "WatchEvent":
        WatchEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "ReleaseEvent":
        ReleaseEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "PullRequestEvent":
        PullRequestEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "IssuesEvent":
        IssuesEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "ForkEvent":
        ForkEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "GollumEvent":
        GollumEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "IssueCommentEvent":
        IssueCommentEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "DeleteEvent":
        DeleteEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "PullRequestReviewCommentEvent":
        PullRequestReviewCommentEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "CommitCommentEvent":
        CommitCommentEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "MemberEvent":
        MemberEvent.append(DatosGeneral[i])
        
for i in range (len(DatosGeneral)):
    if DatosGeneral[i]["type"] == "PublicEvent":
        PublicEvent.append(DatosGeneral[i])
    
booleano = True #Se define un booleano para usarle como condicional del while

while booleano == True: #Para que cada vez que salga de un paso vuelva al menú principal

    #Menú de opciones
    print("""
    ---OPCIONES---
    1). Revisar
    2). Crear
    3). Cerrar programa y crear .json
        """)
    print("")
    eleccion = int(input("¿Qué acción deseas realizar?: ")) #Entrada para que el usuario escoja la acción que desea realizar
    system("cls")

    if eleccion == 1:
        print("----------REVISAR----------")
        print("""
CreateEvent 
PushEvent 
WatchEvent
ReleaseEvent 
PullRequestEvent
IssuesEvent 
ForkEvent
GollumEvent 
IssueCommentEvent
DeleteEvent 
PullRequestReviewCommentEvent 
CommitCommentEvent
MemberEvent 
PublicEvent     
              """)
        print("")
        EventoAVisualizar = str(input("Ingrese el nombre del tipo de eventos que desea revisar: "))
        system("cls")
        
        #=================================================================CREATE EVENT=================================================================
        if EventoAVisualizar == "CreateEvent":
            booleanoteE1 = True
            while booleanoteE1 == True:
                print("CreateEvent")
                for i in range (len(CreateEvent)):
                    print(i+1,"id:",CreateEvent[i]["id"],"id del autor:",CreateEvent[i]["actor"]["id"],"login:",CreateEvent[i]["actor"]["login"],"Avatar:", CreateEvent[i]["actor"]["avatar_url"],"RepoID: ",CreateEvent[i]["repo"]["id"],"RepoName:",CreateEvent[i]["repo"]["name"],"Public:",CreateEvent[i]["public"])

                
                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E1 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E1 == 1:
                    ("---Actualizar---")
                    booleanoAct1 = True
                    while booleanoAct1 == True:
                        IdCreateEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in CreateEvent:
                            if i["id"] == IdCreateEvent:
                                CreateEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                CreateEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                CreateEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                CreateEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                CreateEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdCreateEvent 
                                i["type"]= "CreateEvent" 
                                i["actor"]["id"]= CreateEventIdActor 
                                i["actor"]["login"]= CreateEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = CreateEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= CreateEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= CreateEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct1 = False

                        if i["id"] != IdCreateEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E1 == 2:
                    ("---Eliminar---")
                    booleanoE1 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE1 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar1 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in CreateEvent: #Para que recorrar la lista "CreateEvent"
                            if i["id"] == IdEliminar1: #Si consigue que el id está dento de la lista
                                CreateEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE1 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar1: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E1 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE1 = False
                    system("cls")
                    
        #=================================================================PUSH EVENT=================================================================
        elif EventoAVisualizar == "PushEvent":
            booleanoteE2 = True
            while booleanoteE2 == True:
                print("PushEvent")
                for i in range (len(PushEvent)):
                    print(i+1,"id:",PushEvent[i]["id"],"id del autor:",PushEvent[i]["actor"]["id"],"login:",PushEvent[i]["actor"]["login"],"Avatar:", PushEvent[i]["actor"]["avatar_url"],"RepoID: ",PushEvent[i]["repo"]["id"],"RepoName:",PushEvent[i]["repo"]["name"],"Public:",PushEvent[i]["public"])

                
                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E2 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E2 == 1:
                    ("---Actualizar---")
                    booleanoAct2 = True
                    while booleanoAct2 == True:
                        IdPushEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in PushEvent:
                            if i["id"] == IdPushEvent:
                                PushEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                PushEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                PushEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                PushEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                PushEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdPushEvent 
                                i["type"]= "PushEvent" 
                                i["actor"]["id"]= PushEventIdActor 
                                i["actor"]["login"]= PushEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = PushEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= PushEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= PushEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct2 = False

                        if i["id"] != IdPushEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E2 == 2:
                    ("---Eliminar---")
                    booleanoE2 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE2 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar2 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in PushEvent: #Para que recorrar la lista "PushEvent"
                            if i["id"] == IdEliminar2: #Si consigue que el id está dento de la lista
                                PushEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE2 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar2: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E2 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE2 = False
                    system("cls")
                    
        #=================================================================WATCH EVENT=================================================================
        elif EventoAVisualizar == "WatchEvent":
            booleanoteE3 = True
            while booleanoteE3 == True:
                print("WatchEvent")
                for i in range (len(WatchEvent)):
                    print(i+1,"id:",WatchEvent[i]["id"],"id del autor:",WatchEvent[i]["actor"]["id"],"login:",WatchEvent[i]["actor"]["login"],"Avatar:", WatchEvent[i]["actor"]["avatar_url"],"RepoID: ",WatchEvent[i]["repo"]["id"],"RepoName:",WatchEvent[i]["repo"]["name"],"Public:",WatchEvent[i]["public"])

                
                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E3 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E3 == 1:
                    ("---Actualizar---")
                    booleanoAct3 = True
                    while booleanoAct3 == True:
                        IdWatchEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in WatchEvent:
                            if i["id"] == IdWatchEvent:
                                WatchEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                WatchEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                WatchEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                WatchEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                WatchEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdWatchEvent 
                                i["type"]= "WatchEvent" 
                                i["actor"]["id"]= WatchEventIdActor 
                                i["actor"]["login"]= WatchEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = WatchEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= WatchEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= WatchEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct3 = False

                        if i["id"] != IdWatchEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E3 == 2:
                    ("---Eliminar---")
                    booleanoE3 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE3 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar3 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in WatchEvent: #Para que recorrar la lista "WatchEvent"
                            if i["id"] == IdEliminar3: #Si consigue que el id está dento de la lista
                                WatchEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE3 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar3: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E3 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE3 = False
                    system("cls")
                    
        #=================================================================RELEASE EVENT================================================================= 
        elif EventoAVisualizar == "ReleaseEvent":
            booleanoteE4 = True
            while booleanoteE4 == True:
                print("ReleaseEvent")
                for i in range (len(ReleaseEvent)):
                    print(i+1,"id:",ReleaseEvent[i]["id"],"id del autor:",ReleaseEvent[i]["actor"]["id"],"login:",ReleaseEvent[i]["actor"]["login"],"Avatar:", ReleaseEvent[i]["actor"]["avatar_url"],"RepoID: ",ReleaseEvent[i]["repo"]["id"],"RepoName:",ReleaseEvent[i]["repo"]["name"],"Public:",ReleaseEvent[i]["public"])

                
                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E4 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E4 == 1:
                    ("---Actualizar---")
                    booleanoAct4 = True
                    while booleanoAct4 == True:
                        IdReleaseEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in ReleaseEvent:
                            if i["id"] == IdReleaseEvent:
                                ReleaseEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                ReleaseEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                ReleaseEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                ReleaseEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                ReleaseEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdReleaseEvent 
                                i["type"]= "ReleaseEvent" 
                                i["actor"]["id"]= ReleaseEventIdActor 
                                i["actor"]["login"]= ReleaseEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = ReleaseEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= ReleaseEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= ReleaseEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct4 = False

                        if i["id"] != IdReleaseEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E4 == 2:
                    ("---Eliminar---")
                    booleanoE4 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE4 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar4 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in ReleaseEvent: #Para que recorrar la lista "ReleaseEvent"
                            if i["id"] == IdEliminar4: #Si consigue que el id está dento de la lista
                                ReleaseEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE4 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar4: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E4 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE4 = False
                    system("cls")
                    
        #=================================================================PULL REQUEST EVENT================================================================= 
        elif EventoAVisualizar == "PullRequestEvent":
            booleanoteE5 = True
            while booleanoteE5 == True:
                print("PullRequestEvent")
                for i in range (len(PullRequestEvent)):
                    print(i+1,"id:",PullRequestEvent[i]["id"],"id del autor:",PullRequestEvent[i]["actor"]["id"],"login:",PullRequestEvent[i]["actor"]["login"],"Avatar:", PullRequestEvent[i]["actor"]["avatar_url"],"RepoID: ",PullRequestEvent[i]["repo"]["id"],"RepoName:",PullRequestEvent[i]["repo"]["name"],"Public:",PullRequestEvent[i]["public"])

                
                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E5 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E5 == 1:
                    ("---Actualizar---")
                    booleanoAct5 = True
                    while booleanoAct5 == True:
                        IdPullRequestEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in PullRequestEvent:
                            if i["id"] == IdPullRequestEvent:
                                PullRequestEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                PullRequestEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                PullRequestEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                PullRequestEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                PullRequestEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdPullRequestEvent 
                                i["type"]= "PullRequestEvent" 
                                i["actor"]["id"]= PullRequestEventIdActor 
                                i["actor"]["login"]= PullRequestEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = PullRequestEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= PullRequestEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= PullRequestEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct5 = False

                        if i["id"] != IdPullRequestEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E5 == 2:
                    ("---Eliminar---")
                    booleanoE5 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE5 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar5 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in PullRequestEvent: #Para que recorrar la lista "PullRequestEvent"
                            if i["id"] == IdEliminar5: #Si consigue que el id está dento de la lista
                                PullRequestEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE5 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar5: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E5 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE5 = False
                    system("cls")
                    
        #=================================================================ISSUES EVENT================================================================= 
        elif EventoAVisualizar == "IssuesEvent":
            booleanoteE6 = True
            while booleanoteE6 == True:
                print("IssuesEvent")
                for i in range (len(IssuesEvent)):
                    print(i+1,"id:",IssuesEvent[i]["id"],"id del autor:",IssuesEvent[i]["actor"]["id"],"login:",IssuesEvent[i]["actor"]["login"],"Avatar:", IssuesEvent[i]["actor"]["avatar_url"],"RepoID: ",IssuesEvent[i]["repo"]["id"],"RepoName:",IssuesEvent[i]["repo"]["name"],"Public:",IssuesEvent[i]["public"])

                
                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E6 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E6 == 1:
                    ("---Actualizar---")
                    booleanoAct6 = True
                    while booleanoAct6 == True:
                        IdIssuesEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in IssuesEvent:
                            if i["id"] == IdIssuesEvent:
                                IssuesEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                IssuesEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                IssuesEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                IssuesEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                IssuesEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdIssuesEvent 
                                i["type"]= "IssuesEvent" 
                                i["actor"]["id"]= IssuesEventIdActor 
                                i["actor"]["login"]= IssuesEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = IssuesEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= IssuesEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= IssuesEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct6 = False

                        if i["id"] != IdIssuesEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E6 == 2:
                    ("---Eliminar---")
                    booleanoE6 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE6 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar6 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in IssuesEvent: #Para que recorrar la lista "IssuesEvent"
                            if i["id"] == IdEliminar6: #Si consigue que el id está dento de la lista
                                IssuesEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE6 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar6: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E6 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE6 = False
                    system("cls")
        #=================================================================FORK EVENT================================================================= 
        elif EventoAVisualizar == "ForkEvent":
            booleanoteE7 = True
            while booleanoteE7 == True:
                print("ForkEvent")
                for i in range (len(ForkEvent)):
                    print(i+1,"id:",ForkEvent[i]["id"],"id del autor:",ForkEvent[i]["actor"]["id"],"login:",ForkEvent[i]["actor"]["login"],"Avatar:", ForkEvent[i]["actor"]["avatar_url"],"RepoID: ",ForkEvent[i]["repo"]["id"],"RepoName:",ForkEvent[i]["repo"]["name"],"Public:",ForkEvent[i]["public"])
                
                
                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E7 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E7 == 1:
                    ("---Actualizar---")
                    booleanoAct7 = True
                    while booleanoAct7 == True:
                        IdForkEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in ForkEvent:
                            if i["id"] == IdForkEvent:
                                ForkEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                ForkEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                ForkEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                ForkEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                ForkEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdForkEvent 
                                i["type"]= "ForkEvent" 
                                i["actor"]["id"]= ForkEventIdActor 
                                i["actor"]["login"]= ForkEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = ForkEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= ForkEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= ForkEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct7 = False

                        if i["id"] != IdForkEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E7 == 2:
                    ("---Eliminar---")
                    booleanoE7 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE7 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar7 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in ForkEvent: #Para que recorrar la lista "ForkEvent"
                            if i["id"] == IdEliminar7: #Si consigue que el id está dento de la lista
                                ForkEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE7 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar7: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E7 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE7 = False
                    system("cls")
                    
        #=================================================================GOLLUM EVENT================================================================= 
        elif EventoAVisualizar == "GollumEvent":
            booleanoteE8 = True
            while booleanoteE8 == True:
                print("GollumEvent")
                for i in range (len(GollumEvent)):
                    print(i+1,"id:",GollumEvent[i]["id"],"id del autor:",GollumEvent[i]["actor"]["id"],"login:",GollumEvent[i]["actor"]["login"],"Avatar:", GollumEvent[i]["actor"]["avatar_url"],"RepoID: ",GollumEvent[i]["repo"]["id"],"RepoName:",GollumEvent[i]["repo"]["name"],"Public:",GollumEvent[i]["public"])


                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E8 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E8 == 1:
                    ("---Actualizar---")
                    booleanoAct8 = True
                    while booleanoAct8 == True:
                        IdGollumEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in GollumEvent:
                            if i["id"] == IdGollumEvent:
                                GollumEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                GollumEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                GollumEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                GollumEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                GollumEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdGollumEvent 
                                i["type"]= "GollumEvent" 
                                i["actor"]["id"]= GollumEventIdActor 
                                i["actor"]["login"]= GollumEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = GollumEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= GollumEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= GollumEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct8 = False

                        if i["id"] != IdGollumEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E8 == 2:
                    ("---Eliminar---")
                    booleanoE8 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE8 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar8 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in GollumEvent: #Para que recorrar la lista "GollumEvent"
                            if i["id"] == IdEliminar8: #Si consigue que el id está dento de la lista
                                GollumEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE8 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar8: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E8 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE8 = False
                    system("cls")
                    
        #=================================================================ISSUE COMMENT EVENT=================================================================    
        elif EventoAVisualizar == "IssueCommentEvent":
            booleanoteE9 = True
            while booleanoteE9 == True:
                print("IssueCommentEvent")
                for i in range (len(IssueCommentEvent)):
                    print(i+1,"id:",IssueCommentEvent[i]["id"],"id del autor:",IssueCommentEvent[i]["actor"]["id"],"login:",IssueCommentEvent[i]["actor"]["login"],"Avatar:", IssueCommentEvent[i]["actor"]["avatar_url"],"RepoID: ",IssueCommentEvent[i]["repo"]["id"],"RepoName:",IssueCommentEvent[i]["repo"]["name"],"Public:",IssueCommentEvent[i]["public"])


                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E9 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E9 == 1:
                    ("---Actualizar---")
                    booleanoAct9 = True
                    while booleanoAct9 == True:
                        IdIssueCommentEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in IssueCommentEvent:
                            if i["id"] == IdIssueCommentEvent:
                                IssueCommentEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                IssueCommentEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                IssueCommentEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                IssueCommentEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                IssueCommentEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdIssueCommentEvent 
                                i["type"]= "IssueCommentEvent" 
                                i["actor"]["id"]= IssueCommentEventIdActor 
                                i["actor"]["login"]= IssueCommentEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = IssueCommentEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= IssueCommentEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= IssueCommentEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct9 = False

                        if i["id"] != IdIssueCommentEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E9 == 2:
                    ("---Eliminar---")
                    booleanoE9 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE9 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar9 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in IssueCommentEvent: #Para que recorrar la lista "IssueCommentEvent"
                            if i["id"] == IdEliminar9: #Si consigue que el id está dento de la lista
                                IssueCommentEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE9 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar9: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E9 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE9 = False
                    system("cls")
                    
        #=================================================================DELETE EVENT=================================================================
        elif EventoAVisualizar == "DeleteEvent":
            booleanoteE10 = True
            while booleanoteE10 == True:
                print("DeleteEvent")
                for i in range (len(DeleteEvent)):
                    print(i+1,"id:",DeleteEvent[i]["id"],"id del autor:",DeleteEvent[i]["actor"]["id"],"login:",DeleteEvent[i]["actor"]["login"],"Avatar:", DeleteEvent[i]["actor"]["avatar_url"],"RepoID: ",DeleteEvent[i]["repo"]["id"],"RepoName:",DeleteEvent[i]["repo"]["name"],"Public:",DeleteEvent[i]["public"])


                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E10 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E10 == 1:
                    ("---Actualizar---")
                    booleanoAct10 = True
                    while booleanoAct10 == True:
                        IdDeleteEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in DeleteEvent:
                            if i["id"] == IdDeleteEvent:
                                DeleteEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                DeleteEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                DeleteEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                DeleteEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                DeleteEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdDeleteEvent 
                                i["type"]= "DeleteEvent" 
                                i["actor"]["id"]= DeleteEventIdActor 
                                i["actor"]["login"]= DeleteEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = DeleteEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= DeleteEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= DeleteEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct10 = False

                        if i["id"] != IdDeleteEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E10 == 2:
                    ("---Eliminar---")
                    booleanoE10 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE10 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar10 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in DeleteEvent: #Para que recorrar la lista "DeleteEvent"
                            if i["id"] == IdEliminar10: #Si consigue que el id está dento de la lista
                                DeleteEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE10 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar10: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E10 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE10 = False
                    system("cls")

         #=================================================================PULL REQUEST REVIEW COMMENT EVENT=================================================================
        elif EventoAVisualizar == "PullRequestReviewCommentEvent":
            booleanoteE11 = True
            while booleanoteE11 == True:
                print("PullRequestReviewCommentEvent")
                for i in range (len(PullRequestReviewCommentEvent)):
                    print(i+1,"id:",PullRequestReviewCommentEvent[i]["id"],"id del autor:",PullRequestReviewCommentEvent[i]["actor"]["id"],"login:",PullRequestReviewCommentEvent[i]["actor"]["login"],"Avatar:", PullRequestReviewCommentEvent[i]["actor"]["avatar_url"],"RepoID: ",PullRequestReviewCommentEvent[i]["repo"]["id"],"RepoName:",PullRequestReviewCommentEvent[i]["repo"]["name"],"Public:",PullRequestReviewCommentEvent[i]["public"])

    
                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E11 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E11 == 1:
                    ("---Actualizar---")
                    booleanoAct11 = True
                    while booleanoAct11 == True:
                        IdPullRequestReviewCommentEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in PullRequestReviewCommentEvent:
                            if i["id"] == IdPullRequestReviewCommentEvent:
                                PullRequestReviewCommentEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                PullRequestReviewCommentEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                PullRequestReviewCommentEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                PullRequestReviewCommentEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                PullRequestReviewCommentEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdPullRequestReviewCommentEvent 
                                i["type"]= "PullRequestReviewCommentEvent" 
                                i["actor"]["id"]= PullRequestReviewCommentEventIdActor 
                                i["actor"]["login"]= PullRequestReviewCommentEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = PullRequestReviewCommentEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= PullRequestReviewCommentEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= PullRequestReviewCommentEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct11 = False

                        if i["id"] != IdPullRequestReviewCommentEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E11 == 2:
                    ("---Eliminar---")
                    booleanoE11 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE11 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar11 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in PullRequestReviewCommentEvent: #Para que recorrar la lista "PullRequestReviewCommentEvent"
                            if i["id"] == IdEliminar11: #Si consigue que el id está dento de la lista
                                PullRequestReviewCommentEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE11 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar11: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E11 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE11 = False
                    system("cls")


        #=================================================================COMMIT COMMENT EVENT=================================================================
        elif EventoAVisualizar == "CommitCommentEvent":
            booleanoteE12 = True
            while booleanoteE12 ==True:
                print("CommitCommentEvent")
                for i in range (len(CommitCommentEvent)):
                    print(i+1,"id:",CommitCommentEvent[i]["id"],"id del autor:",CommitCommentEvent[i]["actor"]["id"],"login:",CommitCommentEvent[i]["actor"]["login"],"Avatar:", CommitCommentEvent[i]["actor"]["avatar_url"],"RepoID: ",CommitCommentEvent[i]["repo"]["id"],"RepoName:",CommitCommentEvent[i]["repo"]["name"],"Public:",CommitCommentEvent[i]["public"])


                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E12 = int(input("Ingrese el número de la opción: "))

                if E12 == 1:
                    ("---Actualizar---")
                    booleanoAct12 = True
                    while booleanoAct12 == True:
                        IdCommitCommentEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in CommitCommentEvent:
                            if i["id"] == IdCommitCommentEvent:
                                CommitCommentIdActor = int(input("Ingrese el nuevo id del actor: "))
                                CommitCommentUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                CommitCommentUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                CommitCommentID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                MemberRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdCommitCommentEvent 
                                i["type"]= "CommitComment" 
                                i["actor"]["id"]= CommitCommentIdActor 
                                i["actor"]["login"]= CommitCommentUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = CommitCommentUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= CommitCommentID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]=MemberRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct12 = False

                        if i["id"] != IdCommitCommentEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E12 == 2:
                    ("---Eliminar---")
                    booleanoE12 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE12 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar12 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in CommitCommentEvent: #Para que recorrar la lista "CommitComment"
                            if i["id"] == IdEliminar12: #Si consigue que el id está dento de la lista
                                CommitCommentEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE12 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar12: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E12 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE12 = False
                    system("cls")
        #=================================================================MEMBER EVENT =================================================================
        elif EventoAVisualizar == "MemberEvent":
            booleanoteE13 = True
            while booleanoteE13 == True:
                print("MemberEvent")
                for i in range (len(MemberEvent)):
                    print(i+1,"id:",MemberEvent[i]["id"],"id del autor:",MemberEvent[i]["actor"]["id"],"login:",MemberEvent[i]["actor"]["login"],"Avatar:", MemberEvent[i]["actor"]["avatar_url"],"RepoID: ",MemberEvent[i]["repo"]["id"],"RepoName:",MemberEvent[i]["repo"]["name"],"Public:",MemberEvent[i]["public"])


                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E13 = int(input("Ingrese el número de la opción: "))

                if E13 == 1:
                    ("---Actualizar---")
                    booleanoAct13 = True
                    while booleanoAct13 == True:
                        IdMemberEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in MemberEvent:
                            if i["id"] == IdMemberEvent:
                                MemberEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                MemberEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                MemberEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                MemberEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                MemberRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdMemberEvent 
                                i["type"]= "MemberEvent" 
                                i["actor"]["id"]= MemberEventIdActor 
                                i["actor"]["login"]= MemberEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = MemberEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= MemberEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]=MemberRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct13 = False

                        if i["id"] != IdMemberEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E13 == 2:
                    ("---Eliminar---")
                    booleanoE13 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE13 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar13 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in MemberEvent: #Para que recorrar la lista "MemberEvent"
                            if i["id"] == IdEliminar13: #Si consigue que el id está dento de la lista
                                MemberEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE13 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar13: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E13 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE13 = False
                    system("cls")
      #=================================================================PUBLIC EVENT=================================================================
        elif EventoAVisualizar == "PublicEvent": #Si escoge los "PublicEvent"
            booleanoteE14 = True #Definimos un booleano para usarlo como condicional del while
            while booleanoteE14 == True: #Mientras sea verdadero va a mostrar lo que haya dentro de la lista de "PublicEvent"
                print("PublicEvent")     #Y se mostrará tambien el menú de opciones que hay dentro de esta opción
                for i in range (len(PublicEvent)):
                    print(i+1,"id:",PublicEvent[i]["id"],"id del autor:",PublicEvent[i]["actor"]["id"],"login:",PublicEvent[i]["actor"]["login"],"Avatar:", PublicEvent[i]["actor"]["avatar_url"],"RepoID: ",PublicEvent[i]["repo"]["id"],"RepoName:",PublicEvent[i]["repo"]["name"],"Public:",PublicEvent[i]["public"])

            
                print("""
¿Qué desea realizar?
1. Actualizar
2. Eliminar
3. Continuar                  
""") #Menú de opciones para que sepa lo que puede realizar con este tipo de eventos
                E14 = int(input("Ingrese el número de la opción: ")) #Se crea la entrada para que escoja

                if E14 == 1:
                    ("---Actualizar---")
                    booleanoAct14 = True
                    while booleanoAct14 == True:
                        IdPublicEvent = str(input("Ingrese el ID del elemento que desea actualizar: "))
                        for i in PublicEvent:
                            if i["id"] == IdPublicEvent:
                                PublicEventIdActor = int(input("Ingrese el nuevo id del actor: "))
                                PublicEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
                                PublicEventUrl = input("Ingrese la url: ")
                                NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
                                PublicEventID = int(input("Ingrese el nuevo id del repositorio: "))
                                NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
                                PublicEventRepoUrl = input("Ingrese la url del repositorio: ")
                                NuevoPoP = (input("Ingrese si es publico (True/False): "))
                                
                                i["id"]=IdPublicEvent 
                                i["type"]= "PublicEvent" 
                                i["actor"]["id"]= PublicEventIdActor 
                                i["actor"]["login"]= PublicEventUsuario
                                i["actor"]["gravatar_id"]= ""
                                i["actor"]["url"] = PublicEventUrl
                                i["actor"]["avatar_url"] = NuevoUrlAvatar
                                i["repo"]["id"]= PublicEventID
                                i["repo"]["name"]= NuevoRepoNombre
                                i["repo"]["url"]= PublicEventRepoUrl
                                i["payload"]= {}
                                i["public"] = NuevoPoP

                                print("Evento actualizado!")
                                booleanoAct14 = False

                        if i["id"] != IdPublicEvent:
                            print("Este ID no existe, pruebe con otro")
                            print("")


                if E14 == 2:
                    ("---Eliminar---")
                    booleanoE14 = True #Definimos un booleano para usarlo como condicional del while
                    while booleanoE14 == True: #Mientras sea verdadero se le va a pedir que ingrese el id del evento que desea eliminar
                        IdEliminar14 = str(input("Ingrese el ID del evento que desea eliminar: "))
                        for i in PublicEvent: #Para que recorrar la lista "PublicEvent"
                            if i["id"] == IdEliminar14: #Si consigue que el id está dento de la lista
                                PublicEvent.remove(i) #Se va a eliminar el evento que contenga este ID
                                print("")   
                                print("Evento eliminado con éxito!")
                                print("")
                                input("Presione ENTER para continuar")
                                booleanoE14 = False #El booleano pasa a ser falso y vuelve al menú
                                system("cls")

                        if i["id"] != IdEliminar14: #Si el id no coincide con ninguno de la lista de le pide que vuelva a intentar
                            print("Este ID no existe dentro de este tipo de eventos, por favor vuelva a intentar con uno existente")
                            print("")
                            input("Presione ENTER para continuar") #Como el booleano va a seguir siendo verdadero se le va a volver a pedir que ingrese un id hasta que coincida con alguno de los de la lista

                if E14 == 3:
                    print("")
                    print("Volviendo al menú principal")
                    print("")
                    input("Presione ENTER para continuar")
                    booleanoteE14 = False
                    system("cls")
                    
        else:
            print("Este tipo de evento no existe, intente con uno que esté en el sistema")

        input("Presione ENTER para volver al menú principal")
        system("cls")

    if eleccion == 2:
        print("---Crear---")
        print("""
CreateEvent 
PushEvent 
WatchEvent
ReleaseEvent 
PullRequestEvent
IssuesEvent 
ForkEvent
GollumEvent 
IssueCommentEvent
DeleteEvent 
PullRequestReviewCommentEvent 
CommitCommentEvent
MemberEvent 
PublicEvent     
              """)

        EventoAgregar = input("Ingrese el nombre del evento que desea agregar: ")


        if EventoAgregar == "PublicEvent":
            IDNuevoEvento = (input("Ingrese el ID del evento: "))
            PublicEventIdActor = (input("Ingrese id del actor: "))
            PublicEventUsuario = input("Ingrese el nombre de usuario: ")
            PublicEventUrl = input("Ingrese la url: ")
            UrlAvatar = input("Ingrese la URL del avatar: ")
            PublicEventID = (input("Ingrese el ID del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nombre del repositorio :")
            PublicEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))

            PublicEventAgregar = {
            "id": IDNuevoEvento,
            "type": "PublicEvent",
            "actor": {
                "id": PublicEventIdActor,
                "login": PublicEventUsuario,
                "gravatar_id": "",
                "url": PublicEventUrl,
                "avatar_url": UrlAvatar
            },
            "repo": {
                "id": PublicEventID,
                "name": NuevoRepoNombre,
                "url": PublicEventRepoUrl
            },
            "payload": {},
            "public": NuevoPoP,
            "created_at": "2015-01-01T15:40:33Z"
        }
            
            PublicEvent.append(PublicEventAgregar)

        if EventoAgregar == "MemberEvent":
            IdMemberEventAgregar = input("Ingrese el id del evento: ")
            MemberEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            MemberEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            MemberEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            MemberEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            MemberRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = bool(input("Ingrese si es publico (True/False): "))
        
            MemberEventAgregar = {
            "id": IdMemberEventAgregar,
            "type": "MemberEvent",
            "actor": {
                "id": MemberEventIdActor,
                "login": MemberEventUsuario,
                "gravatar_id": "",
                "url": MemberEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": MemberEventID,
                "name": NuevoRepoNombre,
                "url": MemberRepoUrl
            },
            "public": NuevoPoP,
                }
            
            MemberEvent.append(MemberEventAgregar)

        if EventoAgregar == "CommitCommentEvent": 
            IdCommitCommentEventAgregar = input("Ingrese el id del evento: ")
            CommitCommentIdActor = int(input("Ingrese el nuevo id del actor: "))
            CommitCommentUsuario = input("Ingrese el nuevo nombre de usuario: ")
            CommitCommentUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            CommitCommentIDAgregar = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            CommitCommentRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = bool(input("Ingrese si es publico (True/False): "))

            CommitCommentEventAgregar = {
            "id": IdCommitCommentEventAgregar,
            "type": "CommitCommentEvent",
            "actor": {
                "id": CommitCommentIdActor,
                "login": CommitCommentUsuario,
                "gravatar_id": "",
                "url": CommitCommentUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": CommitCommentIDAgregar,
                "name": NuevoRepoNombre,
                "url": CommitCommentRepoUrl
            },
            "public": NuevoPoP
                }
            
            CommitCommentEvent.append(CommitCommentEventAgregar)
            
        if EventoAgregar == "PullRequestReviewCommentEvent":
            IdPullRequestReviewCommentEventAgregar = input("Ingrese el id del evento: ")
            PullRequestReviewCommentEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            PullRequestReviewCommentEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            PullRequestReviewCommentEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            PullRequestReviewCommentEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            PullRequestReviewCommentEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            PullRequestReviewCommentEventAgregar = {
            "id": IdPullRequestReviewCommentEventAgregar,
            "type": "PullRequestReviewCommentEvent",
            "actor": {
                "id": PullRequestReviewCommentEventIdActor,
                "login": PullRequestReviewCommentEventUsuario,
                "gravatar_id": "",
                "url": PullRequestReviewCommentEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": PullRequestReviewCommentEventID,
                "name": NuevoRepoNombre,
                "url": PullRequestReviewCommentEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            PullRequestReviewCommentEvent.append(PullRequestReviewCommentEventAgregar)
        
        if EventoAgregar == "DeleteEvent":
            IdDeleteEventAgregar = input("Ingrese el id del evento: ")
            DeleteEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            DeleteEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            DeleteEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            DeleteEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            DeleteEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            DeleteEventAgregar = {
            "id": IdDeleteEventAgregar,
            "type": "DeleteEvent",
            "actor": {
                "id": DeleteEventIdActor,
                "login": DeleteEventUsuario,
                "gravatar_id": "",
                "url": DeleteEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": DeleteEventID,
                "name": NuevoRepoNombre,
                "url": DeleteEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            DeleteEvent.append(DeleteEventAgregar)
            
        if EventoAgregar == "IssueCommentEvent":
            IdIssueCommentEventAgregar = input("Ingrese el id del evento: ")
            IssueCommentEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            IssueCommentEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            IssueCommentEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            IssueCommentEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            IssueCommentEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            IssueCommentEventAgregar = {
            "id": IdIssueCommentEventAgregar,
            "type": "IssueCommentEvent",
            "actor": {
                "id": IssueCommentEventIdActor,
                "login": IssueCommentEventUsuario,
                "gravatar_id": "",
                "url": IssueCommentEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": IssueCommentEventID,
                "name": NuevoRepoNombre,
                "url": IssueCommentEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            IssueCommentEvent.append(IssueCommentEventAgregar)
            
        if EventoAgregar == "GollumEvent":
            IdGollumEventAgregar = input("Ingrese el id del evento: ")
            GollumEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            GollumEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            GollumEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            GollumEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            GollumEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            GollumEventAgregar = {
            "id": IdGollumEventAgregar,
            "type": "GollumEvent",
            "actor": {
                "id": GollumEventIdActor,
                "login": GollumEventUsuario,
                "gravatar_id": "",
                "url": GollumEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": GollumEventID,
                "name": NuevoRepoNombre,
                "url": GollumEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            GollumEvent.append(GollumEventAgregar)
            
        if EventoAgregar == "ForkEvent":
            IdForkEventAgregar = input("Ingrese el id del evento: ")
            ForkEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            ForkEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            ForkEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            ForkEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            ForkEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            ForkEventAgregar = {
            "id": IdForkEventAgregar,
            "type": "ForkEvent",
            "actor": {
                "id": ForkEventIdActor,
                "login": ForkEventUsuario,
                "gravatar_id": "",
                "url": ForkEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": ForkEventID,
                "name": NuevoRepoNombre,
                "url": ForkEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            ForkEvent.append(ForkEventAgregar)
            
        if EventoAgregar == "IssuesEvent":
            IdIssuesEventAgregar = input("Ingrese el id del evento: ")
            IssuesEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            IssuesEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            IssuesEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            IssuesEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            IssuesEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            IssuesEventAgregar = {
            "id": IdIssuesEventAgregar,
            "type": "IssuesEvent",
            "actor": {
                "id": IssuesEventIdActor,
                "login": IssuesEventUsuario,
                "gravatar_id": "",
                "url": IssuesEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": IssuesEventID,
                "name": NuevoRepoNombre,
                "url": IssuesEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            IssuesEvent.append(IssuesEventAgregar)
            
        if EventoAgregar == "PullRequestEvent":
            IdPullRequestEventAgregar = input("Ingrese el id del evento: ")
            PullRequestEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            PullRequestEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            PullRequestEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            PullRequestEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            PullRequestEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            PullRequestEventAgregar = {
            "id": IdPullRequestEventAgregar,
            "type": "PullRequestEvent",
            "actor": {
                "id": PullRequestEventIdActor,
                "login": PullRequestEventUsuario,
                "gravatar_id": "",
                "url": PullRequestEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": PullRequestEventID,
                "name": NuevoRepoNombre,
                "url": PullRequestEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            PullRequestEvent.append(PullRequestEventAgregar)        
            
        if EventoAgregar == "ReleaseEvent":
            IdReleaseEventAgregar = input("Ingrese el id del evento: ")
            ReleaseEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            ReleaseEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            ReleaseEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            ReleaseEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            ReleaseEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            ReleaseEventAgregar = {
            "id": IdReleaseEventAgregar,
            "type": "ReleaseEvent",
            "actor": {
                "id": ReleaseEventIdActor,
                "login": ReleaseEventUsuario,
                "gravatar_id": "",
                "url": ReleaseEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": ReleaseEventID,
                "name": NuevoRepoNombre,
                "url": ReleaseEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            ReleaseEvent.append(ReleaseEventAgregar) 
            
        if EventoAgregar == "WatchEvent":
            IdWatchEventAgregar = input("Ingrese el id del evento: ")
            WatchEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            WatchEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            WatchEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            WatchEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            WatchEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            WatchEventAgregar = {
            "id": IdWatchEventAgregar,
            "type": "WatchEvent",
            "actor": {
                "id": WatchEventIdActor,
                "login": WatchEventUsuario,
                "gravatar_id": "",
                "url": WatchEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": WatchEventID,
                "name": NuevoRepoNombre,
                "url": WatchEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            WatchEvent.append(WatchEventAgregar)
            
        if EventoAgregar == "PushEvent":
            IdPushEventAgregar = input("Ingrese el id del evento: ")
            PushEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            PushEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            PushEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            PushEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            PushEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            PushEventAgregar = {
            "id": IdPushEventAgregar,
            "type": "PushEvent",
            "actor": {
                "id": PushEventIdActor,
                "login": PushEventUsuario,
                "gravatar_id": "",
                "url": PushEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": PushEventID,
                "name": NuevoRepoNombre,
                "url": PushEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            PushEvent.append(PushEventAgregar)
            
        if EventoAgregar == "CreateEvent":
            IdCreateEventAgregar = input("Ingrese el id del evento: ")
            CreateEventIdActor = int(input("Ingrese el nuevo id del actor: "))
            CreateEventUsuario = input("Ingrese el nuevo nombre de usuario: ")
            CreateEventUrl = input("Ingrese la url: ")
            NuevoUrlAvatar = input("Ingrese la nuevo URL del avatar: ")
            CreateEventID = int(input("Ingrese el nuevo id del repositorio: "))
            NuevoRepoNombre = input("Ingrese el nuevo nombre del repositorio :")
            CreateEventRepoUrl = input("Ingrese la url del repositorio: ")
            NuevoPoP = (input("Ingrese si es publico (True/False): "))
            
            CreateEventAgregar = {
            "id": IdCreateEventAgregar,
            "type": "CreateEvent",
            "actor": {
                "id": CreateEventIdActor,
                "login": CreateEventUsuario,
                "gravatar_id": "",
                "url": CreateEventUrl,
                "avatar_url": NuevoUrlAvatar
            },
            "repo": {
                "id": CreateEventID,
                "name": NuevoRepoNombre,
                "url": CreateEventRepoUrl
            },
            "public": NuevoPoP
                }
            
            CreateEvent.append(CreateEventAgregar)  
            
        else:
            print("Este evento no existe! Intenta con alguno de los 14 posibles")       
              
            
    if eleccion == 3:
        print("----------CERRANDO PROGRAMA----------")
        print("        NOS VEMOS LUEGO :DDD")        
        NuevoJson = [] #Se guardan los diferentes eventos dentro de una lista para después crear el archivo
        NuevoJson.append(PushEvent)
        NuevoJson.append(WatchEvent)
        NuevoJson.append(ReleaseEvent )
        NuevoJson.append(PullRequestEvent)
        NuevoJson.append(IssuesEvent )
        NuevoJson.append(ForkEvent)
        NuevoJson.append(GollumEvent )
        NuevoJson.append(IssueCommentEvent)
        NuevoJson.append(DeleteEvent )
        NuevoJson.append(PullRequestReviewCommentEvent )
        NuevoJson.append(CommitCommentEvent)
        NuevoJson.append(MemberEvent )
        NuevoJson.append(PublicEvent )
        NuevoJson.append(CreateEvent )
        with open("Actualizado.json",'w',) as f: #Se crea el archivo
            json.dump(NuevoJson,f)
        booleano = False
        CreateEvent 
        
##Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470