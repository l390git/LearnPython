#Imports

# Funktionen
# Aufgabe
def aufgabe():
    # Werte
    a = random.randint(1,10)
    b = random.randint(1,10)

    # Berechung
    erg = a + b
    print("Die Aufgabe:", a, "+", b)
    return erg

# Kommentar
def kommentar(eingabezahl, ergebnis):
    if eingabezahl == ergebnis:
        print(eingabezahl, "ist richtig")
    else:
        print(eingabezahl, "ist falsch")


#Imports
import random
import os

#Init Zufallsgenerator
random.seed()

#Clear Screen
os.system('clear')

#Aufgabe
c = aufgabe()

#Int Variables
versuch=0
zahl=c+1


#Schleife mit while
while zahl != c:

    #Eingabe
    print("Bitte geben Sie eine Zahl ein:")
    z=input()
    try:
        zahl=int(z)
        versuch=versuch+1
    except:
        print("Sie haben keine ganze Zahl eingegeben")
        continue

    kommentar(zahl,c)


#Ende
print("Ergebnis:", c)
print("Anzahl der Versuche:",versuch)
