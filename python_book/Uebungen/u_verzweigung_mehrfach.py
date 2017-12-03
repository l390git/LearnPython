#Umwandlung Brutto in Netto

#Eingaben
#Gehalt
print("Gehalt:")
z=input()
brutto=float(z)

#Steuersatz
print("Steuersatz:")
if brutto <= 2500:
    steuersatz=18
elif brutto > 4000:
    steuersatz=26
else:
    steuersatz=22

#Ausgabe
print("Bruttogehalt:", brutto)
print("Steuersatz:", steuersatz,"%")
print("Steuer:",brutto*steuersatz/100)
print("Netto:",brutto-(brutto*steuersatz/100))
