# Snowman Meltdown

![Python](https://img.shields.io/badge/Python-3.x-blue)

A simple word guessing game where the player tries to guess a hidden word before the snowman melts completely.

The game displays ASCII art stages that change as incorrect guesses are made. The player wins by guessing all letters in the secret word before reaching the mistake limit.


## Features

- Randomly selects a secret word from a given list
- Tracks correct and incorrect guesses
- Displays snowman melting stages
- Validates player input
- Allows replaying the game
- Displays a winning snowman when the player succeeds


## Project Structure

```
📁 Snowman-Meltdown
├── snowman.py     # Main entry point for starting the game
├── game_logic.py  # Core game logic and functions
└── ascii_art.py   # ASCII art used by the game
```

## How to Run

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the game:

```bash
python snowman.py
```


## How to Play

- Enter one letter at a time when prompted.
- Correct guesses reveal letters in the hidden word.
- Incorrect guesses cause the snowman to melt.
- Save the snowman by guessing the word before all stages are lost!


## Requirements
Python 3.x
