#Variable

#Eingaben

#Gehalt
print("Gehalt:")
z=input()
brutto=float(z)

#Familienstand
print("Familienstand;")
familienstand=input()

#Steuersatz
if familienstand=='ledig':
    if brutto>4000:
        steuersatz=26
    else:
        steuersatz=22
else:
    if brutto>4000:
        steuersatz=22
    else:
        steuersatz=18

#Ausgabe
print("Bruttogehalt:", brutto)
print("Steuersatz:", steuersatz,"%")
print("Steuer:",brutto*steuersatz/100)
print("Netto:",brutto-(brutto*steuersatz/100))
