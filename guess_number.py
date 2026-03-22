import sys
import random


def guess_number(name="playerone"):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        player_choice = input(
            f"\n{name},guess which number I'm thinking of ...1,2,3.\n\n"
        )
        if player_choice not in ["1", "2", "3"]:
            print(f"{name},please enter 1,2 or 3")
            return play_guess_number()
        computerchoice = random.choice("123")
        print(f"\n{name}, you chose {player_choice}.")
        print(f"I was thinking about the number{computerchoice}.\n")

        player = int(player_choice)
        computer = int(computerchoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"{name},you win!"
            else:
                return f"Sorry {name}. Better luck next time."

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n Game count:{game_count}")
        print(f"\n{name}'s wins:{player_wins}")
        print(f"\n Your winning percentage:{player_wins/game_count:.2%}")
        print(f"\n Play again,{name}?")
