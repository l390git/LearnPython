# Berechnung einer Summe

summe = 0
for i in range(1, 4):
    fehler = True
    while fehler:
        zahl = input(str(i) + ". Zahl eingeben: ")
        try:
            summe += float(zahl)
            fehler = False
        except:
            print("Das war keine Zahl")
            fehler = True
print("Summe:", summe)
print()
