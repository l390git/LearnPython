#Convert inch in cm
#convert factor inch to cm

factor=2.54

#heading
print("{0:>5}{1:>8}".format("inch","cm"))
for inch in range(10,45,5):
   print("{0:>5.2f}{1:8.2f}".format(inch,inch*factor))
