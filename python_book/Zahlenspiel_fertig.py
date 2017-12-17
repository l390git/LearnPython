
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

# Input
def eingabe():
    i=1
    while i != 0:
        z=input()
        try:
            zahl=int(z)
            i=0
        except:
            print("Sie haben keine ganze Zahl eingegeben")
            continue
    return(zahl)

# Imports
import random
import os

# Init Zufallsgenerator
random.seed()

# Clear Screen
os.system('clear')


# Int Variables
versuch=0
anzahl_aufgaben=0


#Anzahl der Aufgaben
print("Bitte geben Sie die Anzahl der Aufgaben ein:")
anzahl_aufgaben_eingabe=eingabe()

# Schleife Anzahl der Aufgaben
while anzahl_aufgaben != anzahl_aufgaben_eingabe:
    # Aufgabe
    c = aufgabe()
    zahl=c+1

    # Schleife Ergebniss eingabe
    while zahl != c:

        # Eingabe Ergebnis
        print("Was ist das Ergebnis ?:")
        zahl=eingabe()
        versuch=versuch+1
        # Ergebnis ausgeben
        kommentar(zahl,c)

    # Anzahl der Aufgaben hochzählen
    anzahl_aufgaben=anzahl_aufgaben+1

# Ausgabe Ergebnis und Statistik
if anzahl_aufgaben != 0:
    print("Ergebnis:", c)
    print("Anzahl der Versuche:",versuch)
