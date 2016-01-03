import sys
try:
    x=float(sys.argv[1])
    y=float(sys.argv[2])
    print("Programmname:", sys.argv[0])
    print("Erster Parameter:", sys.argv[1])
    print("Erster Parameter:", sys.argv[2])
    print("Ergebniss:", x+y)
except:
    print("Bitte nur Zahlen eingeben !")
