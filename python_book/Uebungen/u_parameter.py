#Funktion

def steuer(x):
    if x>2500:
        steuersatz=22
    else:
        steuersatz=18
    print("Gehalt: ",x,"Steuersatz: ",steuersatz,"Steuerbetrag: ",x*steuersatz/100)

#Hauptprogram
for i in 1800,2200,2500,2900:
    steuer(i)
