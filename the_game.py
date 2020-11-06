"""
This file contains the logic of the game
"""

from random import choice
from verification import check_input_symbols
from verification import check_letters_in_secret_word, win_lost

# encryption printing
def print_word(word: str, letter='') -> str:
    a = ''
    for _, v in enumerate(word):
        if v in letter:
            a += v
        else:
            a += '-'
    return a

# method in which the rules of the game are implemented,
# checking the letters entered by the user, victory or defeat
def game():
    file = open('word_list.txt', 'r')
    word = str(choice(list(file))).strip()
    triers = 8
    answer = ''
    input_list = list()
    while True:
        result = print_word(word, answer)

        if win_lost(word, result, triers) is True:
            file.close()
            break
        else:
            print()
            print('triers: ', triers)
            print(result)

        letter = input('Input a letter: ')

        if check_input_symbols(letter, input_list) is True:
            input_list.append(letter)
            continue

        if check_letters_in_secret_word(letter, word, answer, input_list) is True:
            input_list.append(letter)
            triers -= 1
        else:
            answer += letter
