import json

#Importamos el archivo Json para usarlo dentro del código
with open ('Dia 12/Brayan.json',encoding='utf-8') as openfile:
    DatosGeneral = json.load(openfile)
    
#Listas en las que se van a guardar los valores de los diferentes eventos que hay   
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
    

print("""
-----------MENU DE OPCIONES-----------
1). Revisar
2). Crear
3). Actualizar
4). Borrar
5). Cerrar programa
      """)
print("")
eleccion = int(input("¿Qué acción deseas realizar?: "))

EventoAVisualizar = str(input("Ingrese el nombre del tipo de eventos que desea revisar: "))
for i in range (5):
    print("ash q estrés")
