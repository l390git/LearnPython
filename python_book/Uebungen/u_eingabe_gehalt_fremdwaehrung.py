#Umwandlung Brutto in Netto
kurs=1

#Eingaben
#Gehalt
print("Gehalt:")
z=input()
brutto=float(z)

#Steuersatz
print("Steuersatz:")
z=input()
steuersatz=float(z)

print("Gehalt ist in einer Fremdwährung? (y/n)")
z=input()

if z in "Yy":
    #Umrechnugskurz in €
    print("Umrechnungskurs in Euro:")
    z=input()
    kurs=float(z)


#Ausgabe
print("Bruttogehalt:", brutto)
print("Steuersatz:", steuersatz,"%")
print("Steuer:",brutto*steuersatz/100)
print("Netto in Fremdwährung:",brutto-(brutto*steuersatz/100))
print("Netto in Euro:",(brutto-(brutto*steuersatz/100))*kurs)
