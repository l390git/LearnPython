import sys
try:
    x=float(sys.argv[1])
    y=float(sys.argv[2])
    z=float(sys.argv[3])
    print("Programmname:", sys.argv[0])
    print("Erster Parameter:", x)
    print("Zweiter Parameter:", y)
    print("Dritter Parameter:", z)
    print("Ergebniss:", x+y+z)
except:
    print("Bitte nur Zahlen eingeben !")
