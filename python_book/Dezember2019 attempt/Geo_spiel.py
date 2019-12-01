# Geografiespiel

haupstadt = {"Italien":"Rom", "Spanien":"Madrid",
             "Portugal":"Lissabon"}
hs = haupstadt.items()

for land, stadt in hs:
    eingabe = input("Bitte die Haupstadt von "
                    + land + " eingeben:")
    if eingabe==stadt:
        print("Richtig")
    else:
        print("Falsch, richtig ist:", stadt)