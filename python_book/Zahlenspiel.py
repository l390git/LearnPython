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

#Eingabe
print("Bitte geben Sie eine Zahl ein:")
z=input()
zahl=int(z)

#Verzweigung
if zahl == c:
    print("Zahl ist richtig")
else:
    print("Zahl ist falsch")
    print("Ergebnis:", c)
