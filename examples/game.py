#!/usr/bin/python

DEFAULT_BOARD = 'board.txt'


def load_board(filename):
    board_file = open(filename)
    board = board_file.readlines()
    board_file.close()
    return [row.strip() for row in board]


def display_board(board):
    for row in board:
        print row


def main():
    board = load_board(DEFAULT_BOARD)
    display_board(board)


if __name__ == '__main__':
    main()
