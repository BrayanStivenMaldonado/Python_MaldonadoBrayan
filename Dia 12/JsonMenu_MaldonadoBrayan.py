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
PushEVent = []
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
        PushEVent.append(DatosGeneral[i])
        
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
    3). Cerrar programa
        """)
    print("")
    eleccion = int(input("¿Qué acción deseas realizar?: ")) #Entrada para que el usuario escoja la acción que desea realizar
    system("cls")

    if eleccion == 1:
        print("----------REVISAR----------")
        print("""
CreateEvent 
PushEVent 
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
        if EventoAVisualizar == "CreateEvent":
            print("CreateEvent")
            for i in range (len(CreateEvent)):
                print(i+1,"id:",CreateEvent[i]["id"],"id del autor:",CreateEvent[i]["actor"]["id"],"login:",CreateEvent[i]["actor"]["login"],"Avatar:", CreateEvent[i]["actor"]["avatar_url"],"RepoID: ",CreateEvent[i]["repo"]["id"],"RepoName:",CreateEvent[i]["repo"]["name"],"Public:",CreateEvent[i]["public"])

        elif EventoAVisualizar == "PushEVent":
            print("PushEvent")
            for i in range (len(PushEVent)):
                print(i+1,"id:",PushEVent[i]["id"],"id del autor:",PushEVent[i]["actor"]["id"],"login:",PushEVent[i]["actor"]["login"],"Avatar:", PushEVent[i]["actor"]["avatar_url"],"RepoID: ",PushEVent[i]["repo"]["id"],"RepoName:",PushEVent[i]["repo"]["name"],"Public:",PushEVent[i]["public"])

        elif EventoAVisualizar == "WatchEvent":
            print("WatchEvent")
            for i in range (len(WatchEvent)):
                print(i+1,"id:",WatchEvent[i]["id"],"id del autor:",WatchEvent[i]["actor"]["id"],"login:",WatchEvent[i]["actor"]["login"],"Avatar:", WatchEvent[i]["actor"]["avatar_url"],"RepoID: ",WatchEvent[i]["repo"]["id"],"RepoName:",WatchEvent[i]["repo"]["name"],"Public:",WatchEvent[i]["public"])

        elif EventoAVisualizar == "ReleaseEvent":
            print("ReleaseEvent")
            for i in range (len(ReleaseEvent)):
                print(i+1,"id:",ReleaseEvent[i]["id"],"id del autor:",ReleaseEvent[i]["actor"]["id"],"login:",ReleaseEvent[i]["actor"]["login"],"Avatar:", ReleaseEvent[i]["actor"]["avatar_url"],"RepoID: ",ReleaseEvent[i]["repo"]["id"],"RepoName:",ReleaseEvent[i]["repo"]["name"],"Public:",ReleaseEvent[i]["public"])

        elif EventoAVisualizar == "PullRequestEvent":
            print("PullRequestEvent")
            for i in range (len(PullRequestEvent)):
                print(i+1,"id:",PullRequestEvent[i]["id"],"id del autor:",PullRequestEvent[i]["actor"]["id"],"login:",PullRequestEvent[i]["actor"]["login"],"Avatar:", PullRequestEvent[i]["actor"]["avatar_url"],"RepoID: ",PullRequestEvent[i]["repo"]["id"],"RepoName:",PullRequestEvent[i]["repo"]["name"],"Public:",PullRequestEvent[i]["public"])

        elif EventoAVisualizar == "IssuesEvent":
            print("IssuesEvent")
            for i in range (len(IssuesEvent)):
                print(i+1,"id:",IssuesEvent[i]["id"],"id del autor:",IssuesEvent[i]["actor"]["id"],"login:",IssuesEvent[i]["actor"]["login"],"Avatar:", IssuesEvent[i]["actor"]["avatar_url"],"RepoID: ",IssuesEvent[i]["repo"]["id"],"RepoName:",IssuesEvent[i]["repo"]["name"],"Public:",IssuesEvent[i]["public"])

        elif EventoAVisualizar == "ForkEvent":
            print("ForkEvent")
            for i in range (len(ForkEvent)):
                print(i+1,"id:",ForkEvent[i]["id"],"id del autor:",ForkEvent[i]["actor"]["id"],"login:",ForkEvent[i]["actor"]["login"],"Avatar:", ForkEvent[i]["actor"]["avatar_url"],"RepoID: ",ForkEvent[i]["repo"]["id"],"RepoName:",ForkEvent[i]["repo"]["name"],"Public:",ForkEvent[i]["public"])

        elif EventoAVisualizar == "GollumEvent":
            print("GollumEvent")
            for i in range (len(GollumEvent)):
                print(i+1,"id:",GollumEvent[i]["id"],"id del autor:",GollumEvent[i]["actor"]["id"],"login:",GollumEvent[i]["actor"]["login"],"Avatar:", GollumEvent[i]["actor"]["avatar_url"],"RepoID: ",GollumEvent[i]["repo"]["id"],"RepoName:",GollumEvent[i]["repo"]["name"],"Public:",GollumEvent[i]["public"])

        elif EventoAVisualizar == "IssueCommentEvent":
            print("IssueCommentEvent")
            for i in range (len(IssueCommentEvent)):
                print(i+1,"id:",IssueCommentEvent[i]["id"],"id del autor:",IssueCommentEvent[i]["actor"]["id"],"login:",IssueCommentEvent[i]["actor"]["login"],"Avatar:", IssueCommentEvent[i]["actor"]["avatar_url"],"RepoID: ",IssueCommentEvent[i]["repo"]["id"],"RepoName:",IssueCommentEvent[i]["repo"]["name"],"Public:",IssueCommentEvent[i]["public"])

        elif EventoAVisualizar == "DeleteEvent":
            print("DeleteEvent")
            for i in range (len(DeleteEvent)):
                print(i+1,"id:",DeleteEvent[i]["id"],"id del autor:",DeleteEvent[i]["actor"]["id"],"login:",DeleteEvent[i]["actor"]["login"],"Avatar:", DeleteEvent[i]["actor"]["avatar_url"],"RepoID: ",DeleteEvent[i]["repo"]["id"],"RepoName:",DeleteEvent[i]["repo"]["name"],"Public:",DeleteEvent[i]["public"])

        elif EventoAVisualizar == "PullRequestReviewCommentEvent":
            print("PullRequestReviewCommentEvent")
            for i in range (len(PullRequestReviewCommentEvent)):
                print(i+1,"id:",PullRequestReviewCommentEvent[i]["id"],"id del autor:",PullRequestReviewCommentEvent[i]["actor"]["id"],"login:",PullRequestReviewCommentEvent[i]["actor"]["login"],"Avatar:", PullRequestReviewCommentEvent[i]["actor"]["avatar_url"],"RepoID: ",PullRequestReviewCommentEvent[i]["repo"]["id"],"RepoName:",PullRequestReviewCommentEvent[i]["repo"]["name"],"Public:",PullRequestReviewCommentEvent[i]["public"])

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
                                NuevoPoP = bool(input("Ingrese si es publico (True/False): "))
                                
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
                                i["CommitComment"] = NuevoPoP

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
        ########################################## MEMBER EVENT ##############################################################################3
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
                                NuevoPoP = bool(input("Ingrese si es publico (True/False): "))
                                
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
                                i["MemberEvent"] = NuevoPoP

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

        #=======================================PUBLIC EVENT=================================================================""
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
                                NuevoPoP = bool(input("Ingrese si es publico (True/False): "))
                                
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
                                i["PublicEvent"] = NuevoPoP

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
            


    if eleccion == 3:
        print("----------CERRANDO PROGRAMA----------")
        print("        NOS VEMOS LUEGO :DDD")
        booleano = False