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

#Umrechnugskurz in €
print("Umrechnungskurs in Euro:")
z=input()
kurs=float(z)


#Ausgabe
print("Bruttogehalt:", brutto)
print("Steuersatz:", steuersatz,"%")
print("Steuer:",brutto*steuersatz/100)
print("Netto in S-Dollar:",brutto-(brutto*steuersatz/100))
print("Netto Euro:",(brutto-(brutto*steuersatz/100))*kurs)
