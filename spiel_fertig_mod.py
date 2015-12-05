#Imports
import random
import os
#import time

#init
random.seed()
richtig = 0
#start_time = 0
# 2: Anzahl Aufgaben
anzahl = -1
while anzahl<0 or anzahl>10:
    try:
        print("Wieviele Aufgaben (1 bis 10):")
        anzahl = int(input())
    except:
        continue
#Startzeit nehmen
#start_time = time.process_time()
# 4: Schleife mit "anzahl" Aufgaben
for aufgabe in range(1,anzahl+1):
    # 5: Operatorauswahl
    #opzahl = random.randint(1,4)
    opzahl = 2
    # 6: Operandenauswahl
    if(opzahl == 1):
        a = random.randint(1,30)
        b = random.randint(1,30)
        op = "+"
        c = a + b
    elif(opzahl == 2):
        a = random.randint(1,30)
        b = random.randint(1,30)
        #Negative Ergebnisse verhindern
        if (a < b):
            d = b
            b = a
            a = d
        op = "-"
        c = a - b
    elif(opzahl == 3):
        a = random.randint(1,10)
        b = random.randint(1,10)
        op = "*"
        c = a * b
    # 7: Sonderfall Division
    elif(opzahl == 4):
        c = random.randint(1,10)
        b = random.randint(1,10)
        op = "/"
        a = c * b

    # 8: Aufgabenstellung
    print("Aufgabe", aufgabe, "von",
          anzahl, ":", a, op, b)
    # 9: Schleife mit 3 Versuchen
    for versuch in range(1,4):
        # 10: Eingabe
        try:
            print("Bitte eine Zahl eingeben:")
            zahl = int(input())
        except:
            # Falls Umwandlung nicht erfolgreich
            print("Sie haben keine Zahl eingegeben")
            # Schleife unmittelbar fortsetzen
            continue

        # 11: Kommentar
        if zahl == c:
            os.system('clear')
            #print(zahl, "ist richtig")
            richtig = richtig + 1
            break
        else:
            print(zahl, "ist falsch")


    # 12: Richtiges Ergebnis der Aufgabe
    print("Ergebnis: ", c)
#end_zeit = time.process_time() - start_time

# 13: Anzahl richtige Ergebnisse
print("Richtig:", richtig, "von", anzahl)
#print(end_zeit)
