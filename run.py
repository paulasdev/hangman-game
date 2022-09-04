import random
import string
from words import words
from display import lives_display


def start_game():
    """Start the game and input username"""
    print(""" 
            88        88                                                                                     
            88        88                                                                                     
            88        88                                                                                     
            88aaaaaaaa88  ,adPPYYba,  8b,dPPYba,    ,adPPYb,d8  88,dPYba,,adPYba,   ,adPPYYba,  8b,dPPYba,   
            88""""""""88  ""     `Y8  88P'   `"8a  a8"    `Y88  88P'   "88"    "8a  ""     `Y8  88P'   `"8a  
            88        88  ,adPPPPP88  88       88  8b       88  88      88      88  ,adPPPPP88  88       88  
            88        88  88,    ,88  88       88  "8a,   ,d88  88      88      88  88,    ,88  88       88  
            88        88  `"8bbdP"Y8  88       88   `"YbbdP"Y8  88      88      88  `"8bbdP"Y8  88       88  
                                                    aa,    ,88                                               
                                                    "Y8bbdP"                                                             
    """)
    name = input('Enter your name: \n')
    print(f'Hello, {name}!')
    if input('Would you like to play Hangman? (Y)').upper() == "Y":
        hangman()

    else:
        print('Please try again.')
        start_game()

# function to get random word from list  
def get_valid_word(words):
    """
    Get a random word from words.py
    """
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    """
    Track the correctly word the user input
    """
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 8

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used

        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter:\n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else: 
                lives = lives - 1 
                print('\nYour Letter,', user_letter,'is not in word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')
        
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')

if __name__ == '__main__':
    start_game()