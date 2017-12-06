#Imports
import random

#Init Zufallsgenerator
random.seed()


# Werte
a = random.randint(1,10)
b = random.randint(1,10)

# Berechung
c = a + b
print("Aufgabe:", a, "+", b)
#Schleife mit 4 durchläufen
for i in range(1,10):
    #Eingabe
    print("Bitte geben Sie eine Zahl ein:")
    z=input()
    zahl=int(z)
    #Verzweigung
    if zahl == c:
        print("Zahl ist richtig")
        break
    else:
        print("Zahl ist falsch")

#Ende
print("Ergebnis:", c)
print("Anzahl der Versuche:", i)
