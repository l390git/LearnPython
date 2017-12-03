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

#Mehrfachverzweigung, logische Operatoren

if zahl == c:
    print("Zahl ist richtig")
elif zahl<0 or zahl >100:
    print(zahl, "ist ganz faslch")
elif c-1 <= zahl <= c+1:
    print(zahl, "ist ganz nah dran")
else:
    print("Zahl ist falsch")

#Ende
print("Ergebnis:", c)
