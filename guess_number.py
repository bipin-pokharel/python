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
