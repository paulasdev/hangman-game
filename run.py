import random
import string
from words import words 

def get_value_word(words):
    """
    Get a valid word from the list
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def guess():
    """
    Track the correctly word the user input
    """
    word = get_value_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # Getting user input
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You have already used that character. Please try again.')

    else:
        print('Invalid character. Please try again.')
        

guess()