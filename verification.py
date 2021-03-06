"""
This model has methods for checking the letter entered by the user,
checking the end of the game, checking for the letter in the secret word.
"""

import string


def check_input_symbols(letters: str, input_list: list) -> bool:
    if len(letters) > 1 or len(letters) == 0:
        print("You should input a single letter")
        return True

    if letters in string.digits or letters in string.punctuation or letters in string.ascii_uppercase:
        print("Please enter a lowercase English letter")
        return True

    if letters in input_list:
        print("You've already guessed this letter")
        return True


def check_letters_in_secret_word(letters: str, word: str, answer: str, input_list: list) -> bool:
    if letters not in word:
        print("No such letter in the word")
        return True
    if letters in answer:
        print("You've already guessed this letter")
        return True
    try:
        if input_list[-1] == input_list[-2]:
            print("You've already guessed this letter")
            return True
    except IndexError:
        return False


def win_lost(word: str, answer: str, triers: int) -> bool:
    if answer == word:
        print(f"You guessed the word {word}!\nYou survived!")
        return True
    elif triers == 0:
        print("You lost!")
        return True
