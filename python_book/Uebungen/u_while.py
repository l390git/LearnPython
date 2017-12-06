#Import
import os


#Init
inch=0.1
factor=2.54


os.system('clear')
print("Inch in cm Umrechnung (0 für Ende)")
while inch !=0:
    #Eingabe
    print("Bitte geben sie eine Länge in Inch ein:")
    z=input()
    inch=float(z)
    if inch !=0:
        print(inch,"inch = ",inch*factor,"cm")
    else:
        break
#End
