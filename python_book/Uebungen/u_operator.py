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

if brutto>4000 and familienstand=='ledig':
    steuersatz=26
elif brutto>4000 and familienstand=='verheiratet':
    steuersatz=22
elif brutto<=4000 and familienstand=='verheiratet':
    steuersatz=18
else:
    steuersatz=22


#Ausgabe
print("Bruttogehalt:", brutto)
print("Steuersatz:", steuersatz,"%")
print("Steuer:",brutto*steuersatz/100)
print("Netto:",brutto-(brutto*steuersatz/100))
