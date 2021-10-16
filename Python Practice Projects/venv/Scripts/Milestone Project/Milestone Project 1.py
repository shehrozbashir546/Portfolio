import random

#Displays the board on the users screen
def board_display(board):
    print(board[6]+' | '+board[7]+' | '+board[8])
    print(board[3]+' | '+board[4]+' | '+board[5])
    print(board[0]+' | '+board[1]+' | '+board[2])
#User inputs
def user_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, X or O?  ")
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


test_board = ['#','X','O','X','O','X','O','X','O','X']

place_marker(test_board,'%',8)
board_display(test_board)