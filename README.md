# Guess the Number Game

This repository contains a simple number guessing game built using Python.

## Features
- Randomly generates a number between 0 and 100.
- Player has 10 attempts to guess the correct number.
- Provides hints to guess higher or lower after each attempt.
- Displays all previous guesses after each attempt.

## Dependencies
- Standard Python libraries (no external dependencies).

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Jenishh43/Guess_the_Number.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Guess_the_Number
   ```
3. Run the Python script:
   ```bash
   python guess_the_number.py
   ```

## Usage
- Run the game in your terminal.
- Enter a number between 0 and 100.
- Follow the hints to guess higher or lower.
- Win by guessing the correct number within 10 attempts.

## Code Overview
- **random.randint**: Generates a random number between `MinNum` and `MaxNum`.
- **while loop**: Controls the gameplay and checks the user's guesses.
- **try-except block**: Handles invalid inputs.
- **Game logic**: Provides feedback on each guess and keeps track of previous guesses.

## License
This project is licensed under the MIT License.

## Author
[Jenishh43](https://github.com/Jenishh43)
