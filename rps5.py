import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "\nEnter.. \n1 For Rock, \n2 For Paper, \n3 For Scissors :\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1 , 2 , 3")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
        print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")
        print("")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 you won!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 you won!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return " 🎉you won!"
            elif player == computer:
                return "🫨 Tie game"
            else:
                python_wins += 1
                return "🐍python wins!"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count:" + str(game_count))
        print("\nplayer wins:" + str(player_wins))
        print("\npython wins:" + str(python_wins))

        print("\n")
        print("\n playagain?")

        while True:
            playagain = input("\nPlay again? \nY for YES or \nQ for Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\nCelebrate")
            print("thank you for playing")
            sys.exit("bye")

    return play_rps


play = rps()
play()
