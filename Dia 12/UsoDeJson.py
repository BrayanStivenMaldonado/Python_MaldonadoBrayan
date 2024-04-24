import json

with open('Dia 12/Brayan.json',encoding='utf-8') as openfile:
    miJSON= json.load(openfile)
#print(type(miJSON))
'''
for i in range (5):
  print(miJSON[i])
'''
crearEventos=[]
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])

#print(crearEventos[5]['actor']['id'])

for q in range (5):
    print("#######################")
    print("#### Evento # ",q+1 ,"##")
    print("#######################")
    print("ID: ",crearEventos[q]['id'])
    print("Tipo:",crearEventos[q]['type'])
    print("Actor:")
    print("------- ID:",crearEventos[q]['actor']['id'])

crearEventos[0]['id']=256
print(crearEventos[0]["id"])
#with open("eventos.json","w") as outfile:
    #json.dump(crearEventos,outfile)