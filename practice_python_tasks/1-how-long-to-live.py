# First exercise - Character input
# This is a adjustment where the target age will be asked for and how many time is left until than

# Import system functions for clear screen
import os
import datetime

#Init variables
age=[0,0]

#Clear screen
os.system('clear')

#Input name, age and target age
print("What is your name:")
name=input()


for i in range(0, len(age)):
    if i == 0:
        print("Please tell me your age:")
    else:
        print("Please tell me your target age:")
    z=input()
    try:
        age[i]=int(z)
    except:
        print("You did not specify a number as your age")
        exit()


#State what this program is about
print("This little program will ask for your name, current age and target age. It will show you how much time is left")


#get the current time
now=datetime.datetime.now()

#Output result
print(name, "you will get 100 years old in",now.year+(age[1]-age[0]),"!")
