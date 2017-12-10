#Imports
import random
import os

#Init Zufallsgenerator
random.seed()

#Init Variables
fehler = 1
versuch=0

#Clear Screen
os.system('clear')

# Werte
a = random.randint(1,10)
b = random.randint(1,10)

# Berechung
c = a + b
zahl=c+1


print("Aufgabe:", a, "+", b)
#Schleife mit 4 durchläufen
while zahl != c:
    versuch=versuch+1
    #Eingabe
    while fehler == 1:
        print("Bitte geben Sie eine Zahl ein:")
        z=input()
        try:
            zahl=int(z)
            fehler = 0
        except:
            print("Sie haben keine ganze Zahl eingegeben")

    #Verzweigung
    if zahl == c:
        print("Zahl ist richtig")
        break
    else:
        print("Zahl ist falsch")
    fehler = 1

#Ende
print("Ergebnis:", c)
print("Anzahl der Versuche:",versuch)
