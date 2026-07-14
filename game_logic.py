import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays current game state."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())
    print("Guessed letters:", guessed_letters)
    print("\n")


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []

    print("Welcome to Snowman Meltdown!")

    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess. Try again!")
        else:
            print("Correct!")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nYou saved the snowman!")
            print("The word was: ", secret_word)
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print("\nThe snowman melted...")
    print("The word was: ", secret_word)

