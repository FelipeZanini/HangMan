import random
from words import WORDS_LIST
from hangman import HANGMAN_STAGES


def get_word():
    """
    Get a random word from a list of words.
    """
    word = random.choice(WORDS_LIST).upper()
    return word


def play(word, guessed):
    """
    Responsible for getting the guesses from the user, and assures that
    only single letters or the whole word is input, calling the function
    to display the hangman whether the player failed in his attempt
    or guessed the letter or the mystery word.
    """
    tries = 0
    while len(word) != len(guessed) and tries != 6:
        display_hangman(word, guessed, tries)
        guess = input("\n\nPlease, enter your guess: ").upper()
        if guess == word:
            return tries
        while not guess.isalpha() or len(guess) != 1:
            guess = input("Sorry invalid input, please try again: ").upper()
        if guess not in guessed:
            guessed += [guess for char in word if char == guess]
            if guess not in word:
                tries += 1
        else:
            print("Sorry, that word was already guessed!\n")
    return tries