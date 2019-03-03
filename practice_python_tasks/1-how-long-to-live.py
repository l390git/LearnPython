# First exercise - Character input
# This is a adjustment where the target age will be asked for and how many time is left until than

# Import system functions for clear screen
import os
import datetime

#Init variables
age=[0,0]

#Clear screen
os.system('clear')

#State what this program is about
print("This little program will ask for your name, current age and target age. It will show you how much time is left")

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

#get the current time
now=datetime.datetime.now()
#hoe many years until target age as base
left_years=age[1]-age[0]

#Check if target age is reasonable
if left_years <= 0:
    print("Target age must be higher than your current age of",age[0],"years")
    exit()

#Output result
print(name, "you will get",age[1],"years old in",now.year+left_years,"!")
print("You have",left_years,"years,",left_years*365,"days and",left_years*365*24,"hours left !")
print("These are",left_years*365*24*60,"minutes and",left_years*365*24*60*60,"seconds!")
