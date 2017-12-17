#Imports
import random
import os

#Init Zufallsgenerator
random.seed()

#Init Variables
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
    print("Bitte geben Sie eine Zahl ein:")
    z=input()
    try:
        zahl=int(z)
    except:
        print("Sie haben keine ganze Zahl eingegeben")
        continue

    #Verzweigung
    if zahl == c:
        print("Zahl ist richtig")
        break
    else:
        print("Zahl ist falsch")

#Ende
print("Ergebnis:", c)
print("Anzahl der Versuche:",versuch)
