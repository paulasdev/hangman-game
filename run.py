import random
from words import words 

def get_value_word(words):
    """ 
    Get a valid word from the list
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word
