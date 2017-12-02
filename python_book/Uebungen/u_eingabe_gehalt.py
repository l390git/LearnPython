#Umwandlung Brutto in Netto

#Eingaben
#Gehalt
print("Gehalt:")
z=input()
brutto=float(z)

#Steuersatz
print("Steuersatz:")
z=input()
steuersatz=float(z)

#Ausgabe
print("Bruttogehalt:", brutto)
print("Steuersatz:", steuersatz,"%")
print("Steuer:",brutto*steuersatz/100)
print("Netto:",brutto-(brutto*steuersatz/100))
