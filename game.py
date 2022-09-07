import random
import string
from words import words
from display import lives_display

def start_game():
    
    """
    Start the game and input username
    """
    print("""
             _  _  __  __  _  __ __ __  __  __  _  
            | || |/  \|  \| |/ _]  V  |/  \|  \| | 
            | >< | /\ | | ' | [/\ \_/ | /\ | | ' | 
            |_||_|_||_|_|\__|\__/_| |_|_||_|_|\__|       
    """)


    if input('Would you like to play Hangman? (Y)').upper() == "Y":
        username()

    else:
        print('Please try again.')
        start_game()

def username ():
    name = input('Enter your name: \n')
    print(f'Hello, {name}!')
    # if input('Would you like to play Hangman? (Y)').upper() == "Y":
    hangman()

    # else:
    #     print('Please try again.')
    #     start_game()

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

    lives = 6

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
     

        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_display[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter:\n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            

            else: 
                lives = lives - 1 
                print('\nYour Letter,', user_letter,'is not in word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')
        
    if lives == 0:
        print(lives_display[lives])
        print('You died, sorry. The word was', word)
        play_again()
    else:
        print('You guessed the word', word, '!!')
        play_again()



def play_again():
    "Option to start the game"
    play_again = False

    while not play_again:
        restart = input("Would you like to play again? (Y/N)\n").upper()
        if restart == "Y":
            play_again = True
            hangman()
        
        elif restart == "N":
             play_again = True
             print("Goodbye!")
             start_game()
        else:
            print("Please select the right option.")