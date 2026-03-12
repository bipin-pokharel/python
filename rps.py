import sys
import random

print("")
playerchoice = input("Enter.. \n1 For Rock, \n2 For Paper, \n3 For Scissors :")

player = int(playerchoice)

if player < 1 | player > 3:
    print("You must enter 1 , 2 , 3")

computerchoice = random.choice("123")
computer = int(computerchoice)

print("")
print("You chose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")
