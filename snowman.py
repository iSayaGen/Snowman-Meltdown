"""Entry point for the Snowman Meltdown game.

Starts the game by calling the play_game function
from the game_logic module.
"""

from game_logic import play_game

if __name__ == "__main__":
    while True:
        play_game()

        again = input("\nPlay again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break