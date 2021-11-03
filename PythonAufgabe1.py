import logging
from post import checkMission # Diese Zeile bitte nicht verändern
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
logging.basicConfig(filename='example.log',level=logging.INFO)
'''
Ihre Aufgabe, sollten Sie sie akzeptieren lautet: Suchen sie in der nachfolgenden Textdatei nach dem Wort "Mission"
und lösen Sie das Coderätsel. Die Missionen steigen im Schwierigkeitsgrad an. Das Ergebnis der Knobelaufgabe muss immer in der Variable a
gespeichert werden. Viel Erfolg! Bitte scheuen Sie sich nicht fragen zu stellen, sollten Sie einmal nicht weiterkommen.
Tragen Sie bitte zunächst Ihre Teamnummer in Zeile 9 ein. Diese wird Ihnen von Ihrem Instructor zugewiesen.

'''
team='1' # Tragen Sie in dieser Zeile bitte Ihre Teamnummer ein.
'''
# Eine einfache Ausgabe auf dem Terminal
# Mission 1 - Setzen Sie die Variable a auf den Wert 'Ich bin im Kurs DPPP und mache eine kurze Fingerübung in Python' Lassen Sie diesen auf der Konsole ausgeben.
# Arbeiten Sie hierzu mit einem 'print()' Statement
'''

def mission1():
    
    a='' #Diese Variable ist zu setzen
    Ergebnis1=checkMission('Ich Bin ein Text',10,6)
    print ('############################################')
    print (Ergebnis1)
    Ergebnis=checkMission(a,team,1) # Diese Zeile bitte nicht verändern
    logging.warning('Dies soll eine Warnung für Euch sein')
    logging.info('I told you so')  # will not print anything
    return Ergebnis

'''
# Mission 2 - addieren Sie zwei Zahlen! Das Ergebnis sollte 100 lauten. Nutzen Sie hierzu
'''
def mission2():

    Summand1 = 0
    Summand2 = 0

    a=0 # Hier sollte Ihre Rechenvorschrift stehen verwenden Sie bitte die beiden Summanden- Hier einfach nur 100 hinzuschreiben ist geschummelt ;)
    
    Ergebnis=checkMission(a,team,2) # Diese Zeile bitte nicht verändern
    return Ergebnis # Diese Zeile bitte nicht verändern
'''
# Mission 3 - auch Texte können zusammengesetzt werden. Versuchen Sie einmal zwei Textschnipsel zu addieren- Man nennt Dies 'concetanation' oder 'Verkettung
'''
def mission3():
    Text1='Texte verketten '
    Text2='funktioniert wunderbar'
    
    a='' #Hier kommt Ihre Funktion hinein
    
    #print (a)
    
    Ergebnis=checkMission(a,team,3) # Diese Zeile bitte nicht verändern
    return Ergebnis # Diese Zeile bitte nicht verändern

'''
# Mission 4: Vergleichsoperatoren.
Vergleichsoperatoren wie kleiner als '<'
oder größer als '>' sind ihnen bekannt- wie sieht es aber mit '<=' oder '==' aus ? In der Programmierung muss man recht häufig
Werte vergleichen. Eine Übersicht der so genannten boolschen Operatoren finden Sie hier:
kleiner als -> '<'
größer als -> '>'
exakt gleich -> '=='
größer gleich -> '>='
kleiner gleich -> '<='

Vergleichsoperatoren lernt man üblicherweise in einfachen 'Wenn, dann' Verknüpfungen kennen. Die erste einfache Aufgabe lautet:
Setzen Sie Ihren Ausgabewert a auf den Textinhalt 'kleiner', sobald die Variable zahl <= 6 ist.
'''
def mission4():
    zahl = 6
    a=0

    # Verändern Sie das folgende If Statement, um die Anforderung passend zu ergänzen.
    # Denken Sie daran, die Variable a innerhalb des Statements passend zu setzen.
    if zahl == 0:
        print(zahl, "ist gleich 0")
        # Hier gehört noch etwas hin- es könnte so aussehen: a = größer
    Ergebnis=checkMission(a,team,4) # Diese Zeile bitte nicht verändern
    return Ergebnis # Diese Zeile bitte nicht verändern
'''
Mission 5: Eine einfache "while" Schleife
Schleifen sind ein wichtiges Werkzeug, wenn es beispielsweise darum geht, alle Werte einer Datei einzulesen.
Die Anweisung beim einlesen einer Datei lautet dann in etwa: Lies solange Zeilen einer Datei ein, solange Zeilen da sind.
Eine Schleife benötigt also eine Abbruchbedingung. In den gängigen Programmiersprachen
gibt es unnterschiedliche Arten von Schleifen. Die folgende Aufgabe nutzt eine while Schleife.
Die Abbruchbedingung wird direkt an den Befehl while angehängt.
Beispielsweise so:

i=0
while i<=10:
    i=i+1

Die Schleife wird solange durchlaufen, solange der Wert von i kleiner gleich 10 ist.
Mit jedem Schleifendurchlauf wird der Wert i um eins erhöht.
Ist der Wert i=10 erreicht, wird die Schleife beendet.

Aufgabe: Gestalten Sie die untenstehende while Schleife so um, daß diese exakt 20 mal durchlaufen wird.
Der Wert von s soll dabei jedes mal verdoppelt werden.
'''
def mission5():
    '''
    Beschreibung
    '''
    a=19 # Diesen Wert nicht verändern
    i=0

    while i >= 100: #Stimmt diese Anweisung ?
        a=2         #Hier muss bestimmt auch etwas verändert werden.
        i=i+1

        

    Ergebnis=checkMission(a,team,5) # Diese Zeile bitte nicht verändern
    return Ergebnis # Diese Zeile bitte nicht verändern

def mission6():
    '''
    Ich brauche eine schöne Beschreibung, was diese Funktion macht...
    '''
    Satz=['Diese','Aufgabe','zerstört','sich','in','10','Sekunden','selbst'] # Die eckigen Klammern initialisieren ein Array

    for Wort in Satz:
        print (Wort)

    Ergebnis=checkMission(Satz,team,6) # Diese Zeile bitte nicht verändern
    return Ergebnis # Diese Zeile bitte nicht verändern


print('Team '+str(team)+ ' Fortschritt:')
print ('Mission 1 Status: '+ mission1())
print ('Mission 2 Status: '+ mission2())
print ('Mission 3 Status: '+ mission3())
print ('Mission 4 Status: '+ mission4())
print ('Mission 5 Status: '+ mission5())
#print ('Mission 6 Status: '+ mission6())
