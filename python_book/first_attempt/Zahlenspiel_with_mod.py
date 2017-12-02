#Zufallsgenerator
import random
import Zahlenspiel_with_modules as zwm
random.seed()
#Init Variables here
zahl = 0
versuch = 0

#Funktionen sind im Modul
c = zwm.aufgabe()
#Eingabe
while zahl != c:
    versuch = versuch + 1
    #Eingabe
    print("Bitte eine Zahl eingeben:")
    z = input()
    try:
        zahl = int(z)
    except:
        print("Sie haben keine Zahl eingeben")
        continue
    zwm.kommentar(zahl, c)
#Ende
print("Ergebnis:", c)
print("Anzahl der Versuche:", versuch)
