#from dotenv import load_dotenv
#load_dotenv()
import requests
#import os
#from requests_toolbelt.multipart.encoder import MultipartEncoder



# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.

def checkMission(text,team,mission):

    team=team
    text=str(text)
    mission=mission
    posttext='Team '+ str(team) +' schloss Mission '+ str(mission) +' ab. Das Ergebnis lautet: '+str(text)

    if mission==1 and text=='Ich bin im Kurs DPPP und mache eine kurze Fingerübung in Python':
        post(posttext)
        return 'Mission 1 erfolgreich'
    elif mission==2 and text=='100':
        post(posttext)
        return 'Mission 2 erfolgreich'
    elif mission==3 and text=='Texte verketten funktioniert wunderbar':
        post(posttext)
        return 'Mission 3 erfolgreich'
    elif mission==4 and text=='kleiner':
        post(posttext)
        return 'Mission 4 erfolgreich'
    elif mission==5 and text=='19922944':
        post(posttext)
        return 'Mission 5 erfolgreich'
    elif mission==5 and text=='39845888':
        post(posttext)
        return 'Achtung die Schleife wurde einmal zu oft durchlaufen'
    else:
        return 'Noch nicht abgeschlossen'

def post(text):
    access_token ='ZTg2ZTBiMjMtM2M2ZC00ZjlmLWIwZWEtMjU3NzEzOGZiMmNlMGVlYmZhOTItN2E5_PF84_b26cc13b-37f7-4057-ab70-3e0f679db605'
    #room_ID = os.getenv("ROOMID")
    room_ID = 'Y2lzY29zcGFyazovL3VzL1JPT00vZmI2NDY1YTAtNDM2OS0xMWViLWJkMjQtY2RiOWU4M2Y5ZTVj'
    apiUrl = "https://webexapis.com/v1/messages"
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    body = {"roomId" : room_ID, "text" : text}
    requests.post(url=apiUrl, json=body, headers=httpHeaders)
    #response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

def postimage(image):

    #access_token = os.getenv("ACCESSTOKEN")
    access_token ='YjVkNTFjOWMtOThhOS00ODJiLWIwZTEtMDRlNWViZDkwNjU3MTJhNmZjZDctNTM4_PF84_b26cc13b-37f7-4057-ab70-3e0f679db605'
    #room_ID = os.getenv("ROOMID")
    room_ID = 'Y2lzY29zcGFyazovL3VzL1JPT00vZmI2NDY1YTAtNDM2OS0xMWViLWJkMjQtY2RiOWU4M2Y5ZTVj'
    
    payload={'roomId': room_ID,'text': 'Der aktuelle Missionsstand'}
    files=[('files',(image,open(image,'rb'),'image/png'))]
    apiUrl = "https://api.ciscospark.com/v1/messages"
    httpHeaders = {"Authorization" : "Bearer " + access_token}
    #body = {"roomId" : room_ID, "text" : "Der aktuelle Missionsstand","files":files}
    response = requests.request("POST", apiUrl, headers=httpHeaders, data=payload, files=files)
    print(response.status_code)
    print(response.text)
