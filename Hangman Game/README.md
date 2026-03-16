# Hangman Game

A fun and interactive command-line Hangman game built using Python.

This project allows the user to guess a hidden word one letter at a time. For every wrong guess, the player loses one life, and the Hangman ASCII art progresses step by step. The game continues until the player either guesses the complete word correctly or runs out of lives.

The project demonstrates Python fundamentals such as loops, conditionals, lists, string handling, user input, random word selection, and modular programming using multiple files.

## Features

- Random word selection from a predefined word list
- User guesses one letter at a time
- Tracks correct guesses
- Reduces lives for wrong guesses
- Displays the current word progress after each guess
- Prevents confusion by showing already guessed letters
- Uses ASCII art stages to visually represent game progress
- Shows win and lose messages at the end of the game

## Technologies Used

- Python
- Random module
- Loops
- Conditional statements
- Lists
- Strings
- User input handling
- Modular Python files

## Project Structure

hangman-game  
├── main.py  
├── hangman_words.py  
├── hangman_art.py  

## How It Works

1. The program randomly selects a word from the word list.
2. The player starts with 6 lives.
3. The player guesses one letter at a time.
4. If the guessed letter is correct, it is revealed in the word.
5. If the guessed letter is wrong, one life is lost.
6. The Hangman ASCII art updates after each wrong guess.
7. The game ends when the player guesses the full word or loses all lives.

## Learning Outcomes

Through this project, I learned how to:

- Work with Python modules and import files
- Use the random module to select words
- Build game logic using loops and conditionals
- Track correct guesses using lists
- Update and display dynamic output
- Create a simple terminal-based game
- Organize code into separate files for better structure

## Conclusion

This project is a simple and engaging Python game that helps strengthen programming basics through real-time user interaction and game logic implementation. It is a great beginner-friendly project for practicing Python in a fun way.
