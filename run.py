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
    Track the correctly word the user guess
    """
    word = get_value_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

user_input = input('Type somenthing: ')
print(user_input)