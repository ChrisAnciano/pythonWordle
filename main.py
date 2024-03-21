''' Christopher Anciano 4/4/23
This program is a word guessing game inspired by Wordle. Players have six attempts to guess a random 5-letter word. 
After each guess, the program provides feedback on the correctness of each letter. 
If the player guesses the word correctly within six attempts, they win; otherwise, the correct word is revealed. Players can choose to play again or exit the game.
'''

import random
import sys
from termcolor import colored
import nltk
nltk.download('words')
from nltk.corpus import words

def print_menu():
    '''Prints the game menu.'''
    print("Let's play Wordle:")
    print("Type a 5 letter word and hit enter!\n")

# nltk data path
nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]
print(len(words_five))
print_menu()
play_again = ""
while play_again != "q":
    word = random.choice(words_five).lower() # Choose a random 5-letter word
    for attempt in range(1, 7):
        guess = input().lower() # Read player's guess

        sys.stdout.write('\x1b[1A') # Move cursor up one line
        sys.stdout.write('\x1b[2K') # Clear the line

        for i in range(min(len(guess), 5)): # Display feedback on correctness of each letter
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word: # Check if player guessed the word
            print(colored(f"Congrats! You got the wordle in {attempt}", 'red'))
            break
        elif attempt == 6:
            print(f"Sorry the wordle was.. {word}")
    play_again = input("Want to play again? Type q to exit.")

print("Goodbye!")
