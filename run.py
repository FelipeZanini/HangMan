import random
from words import WORDS_LIST
from hangman import HANGMAN_STAGES


def get_word():
    """
    Get a random word from a list of words.
    """
    word = random.choice(WORDS_LIST).upper()
    return word