#Zufallsgenerator
import random
random.seed()
#Init Variables
zahl = 0
versuch = 0

#Funktionen
def aufgabe():
    a = random.randint(1,10)
    b = random.randint(1,10)
    erg = a + b
    print("Die Aufgabe:",a,"+",b)
    return erg

def kommentar(eingabezahl, ergebnis):
    versuch = versuch + 1
    if eingabezahl == ergebnis:
        print(eingabezahl, "ist richtig !")
    else:
        print(eingabezahl, "ist falsch")
c = aufgabe()

#Eingabe
while zahl != c:
    #versuch = versuch + 1
    #Eingabe
    print("Bitte eine Zahl eingeben:")
    z = input()
    try:
        zahl = int(z)
    except:
        print("Sie haben keine Zahl eingeben")
        continue
    kommentar(zahl, c)
#Ende
print("Ergebnis:", c)
print("Anzahl der Versuche:", versuch)
