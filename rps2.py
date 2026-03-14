import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True
while playagain:

    playerchoice = input("\nEnter.. \n1 For Rock, \n2 For Paper, \n3 For Scissors :\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1 , 2 , 3")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")
    print("")

    if player == 1 and computer == 3:
        print("🎉 you won!")
    elif player == 2 and computer == 1:
        print("🎉 you won!")
    elif player == 3 and computer == 2:
        print(" 🎉you won!")
    elif player == computer:
        print("🫨 Tie game")
    else:
        print("🐍python wins!")

    playagain = input("\nPlay again? \nY for YES or \nQ for Quit")
    if playagain.lower() == "y":
        continue
    else:
        print("\nCelebrate")
        print("thank you for playing")
        playagain = False

sys.exit("bye")
