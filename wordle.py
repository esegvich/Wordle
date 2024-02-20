'''
Ethan Segvich
CS 1210
Wordle Final Project
'''

import random
from termcolor import colored
import csv

def read_random_word():
    with open("words.txt") as f:
        word_lines = f.read().splitlines()
        words = [line.split(',')[0] for line in word_lines]
        return random.choice(words)

def is_valid_input(guess):
    return len(guess) == 5

def get_hint(word):
    with open("words.txt") as f:
        word_lines = f.read().splitlines()
        for line in word_lines:
            hints = line.split(',')
            if hints[0] == word:
                return hints[1]

def play_wordle():
    guess_list = []
    word = read_random_word()
    print(word)

    guess = str(input("\nEnter your guess: ")).lower()
    guess_list.append(guess)

    while not is_valid_input(guess):
        print("Invalid input. Please enter a valid 5-letter word.")
        guess = str(input("Enter your guess: ")).lower()

    guess_count = 1

    while guess != word:
        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        print()

        guess = str(input("Enter your guess: ")).lower()
        if guess == 'n':
            break
        guess_list.append(guess)
        guess_count += 1

        while not is_valid_input(guess):
            print("Invalid input. Please enter a valid 5-letter word.")
            guess = str(input("Enter your guess: ")).lower()

        if guess_count == 5 and guess != word:
            user_hint = input("Would you like a hint? (y/n): ").lower()
            if user_hint == 'y':
                hint = get_hint(word)
                print(hint)

        if guess_count == 6 and guess != word:
            print("You ran out of guesses.")
            print(f"The word was {word}")
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == 'y':
                play_wordle()
            else:
                print("Thanks for playing!")
                return

    if guess == word:
        print("You win!")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            play_wordle()
        else:
            print("Thanks for playing!")
 
user_play = input("Would you like to play Wordle? (y/n) ")

while user_play.lower() != "n":
    if user_play.lower() == "y":
        print("Welcome to Wordle!")
        print("You have 6 tries to guess the 5 letter word.")
        print("Each guess must be a valid 5 letter word.")
        print("After each guess, the color of the tiles will change to show how close your guess was to the word.")
        print("\nGreen = Correct letter in correct place.")
        print("Yellow = Correct letter in wrong place.")
        print("Grey = Letter not in word.")

        play_wordle()

    else:
        print("Invalid input. Please enter 'y' or 'n'.")

    user_play = input("Would you like to play Wordle? (y/n) ")

print("Have a nice day!")