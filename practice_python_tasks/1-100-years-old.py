# First exercise - Character input

# Import system functions for clear screen
import os
import datetime

#Init variables
age=0

#Clear screen
os.system('clear')

#State what this program is about
print("This little program will ask for your name and age and tell you in which year you will turn 100!")

#Input name and age
print("What is your name:")
name=input()

print("Please tell me your age:")
z=input()
try:
    age=int(z)
except:
    print("You did not specify a number as your age")
    exit()

#get the current time
now=datetime.datetime.now()

#Output result
print(name, "you will get 100 years old in",now.year+(100-age),"!")
