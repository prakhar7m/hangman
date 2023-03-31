# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import re

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if all(letter in letters_guessed for letter in secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_copy = secret_word
    for letter in secret_word_copy:
        if letter not in letters_guessed:
            secret_word_copy = secret_word_copy.replace(letter, ' _ ')
    return secret_word_copy


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase
    for letter in letters_guessed:
        if letter in available_letters:
            available_letters = available_letters.replace(letter, '')
    return available_letters



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    current_state = len(secret_word) * [" _ "]
    result = ' '.join(current_state)
    letters_guessed = []
    unique = set(secret_word)
    print("Welcome to the game Hangman")
    print(f"I am thinking of a {len(secret_word)} letter word.")
    print(f"Your word is: {result}")
    print("You have 6 guesses left")

    warnings_counter = 3
    guess = 6
    while True:
        print('------------------------------------------')
        print(f"available letters: {get_available_letters(letters_guessed)}")
        input_str = input('Please guess a letter: ')
        if not re.match("^[a-zA-Z*]*$", input_str):
            warnings_counter -= 1
            print(f"Error! Only alphabets allowed! You have {warnings_counter} warnings left")

        elif len(input_str) > 1:
            warnings_counter -= 1
            print(f"Error! Only 1 character allowed! You have {warnings_counter} warnings left.")

        elif input_str in letters_guessed:
            print(f'this letter has already been guessed')
            warnings_counter -= 1
            print(f"Error! You lose a warning! You have {warnings_counter} warnings left.")

        if warnings_counter == 0:
            guess -= 1
            print(f'You lose a guess. You have {guess} guess left.')
            warnings_counter = 3

        if input_str == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))

        if str.isalpha(input_str) and input_str not in letters_guessed:
            input_str = str.lower(input_str)
            letters_guessed.append(input_str)

            if input_str in secret_word:
                a = [i for i, letter in enumerate(secret_word) if letter == input_str]
                for num in a:
                    current_state[num] = input_str
                    result = ' '.join(current_state)
                print(f'Good Guess: {result}')

                if is_word_guessed(secret_word, letters_guessed):
                    print(f'you win. Your score is {guess * len(unique)}')
                    break
                else:
                    print(f"You have {guess} guess left")
                    continue

            else:
                print(f'Oops! That letter is not in my word: {result}')
                guess -= 1
                print(f'You have {guess} guess left')

        if guess == 0:
            print(f'you lose. The word is {secret_word}')
            break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    my_dict = {}
    other_dict = {}

    if len(my_word) != len(other_word):
        return False

    for i, letter in enumerate(my_word):
        if letter != "_":
            my_dict[i] = letter

    for i, letter in enumerate(other_word):
        other_dict[i] = letter

    if my_dict.items() <= other_dict.items():
        for key in other_dict:
            if key not in my_dict:
                return True if other_dict[key] not in my_dict.values() else False

    else:
        return False


def show_possible_matches(my_word):
    for word in wordlist:
        if match_with_gaps(my_word, word) is True:
            print(word)

    '''

    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

