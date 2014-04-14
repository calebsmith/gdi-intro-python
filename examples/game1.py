#!/usr/bin/python
"""
This is a simple text based game that displays a board and obtains input from
the command line.


In this stage, the following is already implemented:
    * Loads a text file as the playing board
    * Displays the board and obtains input in a loop until a user types `quit`


The following needs to be implemented:
    * Display the player on the board
    * Move the player on the board when the user types input such as "up"
"""
from __future__ import print_function


DEFAULT_BOARD = 'board.dat'
PLAYER_X_START = 5
PLAYER_Y_START = 5


def print_char(char):
    """Print only the given `char` without a newline"""
    print(char, end='')


def get_input():
    try:
        move = raw_input("Choose a direction (Type `quit` to quit): ")
    except NameError:
        # Python3
        move = input("Choose a direction (Type `quit` to quit): ")
    return move


def load_board(filename):
    """
    Given a filename of a text file, load the characters therein and return as
    a list of character lists. E.g.:

    A file containing:
        xox
        oxx
        oxo

    would return:
        [
            ['x', 'o', 'x'],
            ['o', 'x', 'x'],
            ['o', 'x', 'o'],
        ]
    """
    board_file = open(filename)
    board_tiles = []
    for line in board_file.readlines():
        board_tiles.append([char for char in line.strip()])
    board_file.close()
    return board_tiles


def get_tile(board, x, y):
    """
    Returns the character for a give, `x` and `y` position of the given `board`
    """
    return board[y][x]


def display(board, player_x, player_y):
    """
    Display the given `board` and the player at the position `player_x` and
    `player_y`
    """
    for y, row in enumerate(board):
        for x, tile in enumerate(row):
            # FIXME: Insert code here to display player
            print_char(tile)
        print_char('\n')


def main():
    # Load the board and set the player at the starting position
    board = load_board(DEFAULT_BOARD)
    player_x = PLAYER_X_START
    player_y = PLAYER_Y_START
    while True:
        # Display the board and player
        display(board, player_x, player_y)
        # Obtain and handle user input
        move = get_input()
        # FIXME: Insert code here to handle the 'move' the player has made.
        # (Hint: should manipulate player_x and player_y)
        if move == 'quit':
            return True


if __name__ == '__main__':
    main()
