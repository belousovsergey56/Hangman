#!/usr/bin/python3

from the_game import game

GAME_NAME = 'H A N G M A N'


def greeting():
    print(GAME_NAME)


def start_game():
    while True:
        user_input =\
        input("""Type "play" to play the game, "exit" to quit: """)
        if user_input == 'play':
            game()
            print()
        elif user_input == 'exit':
            break
        else:
            continue


if __name__ == '__main__':
    greeting()
    start_game()
