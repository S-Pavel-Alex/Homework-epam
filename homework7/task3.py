from typing import List


def combination_x_winner(board: List[List]):
    if board[0][0] == board[0][1] == board[0][2] == 'x' or \
     board[1][0] == board[1][1] == board[1][2] == 'x' or \
     board[2][0] == board[2][1] == board[2][2] == 'x' or \
     board[0][0] == board[1][0] == board[2][0] == 'x' or \
     board[0][1] == board[1][1] == board[2][1] == 'x' or \
     board[0][2] == board[1][2] == board[2][2] == 'x' or \
     board[0][0] == board[1][1] == board[2][2] == 'x' or \
     board[0][2] == board[1][1] == board[2][0] == 'x':
        return True


def combination_o_winner(board: List[List]):
    if board[0][0] == board[0][1] == board[0][2] == 'o' or \
     board[1][0] == board[1][1] == board[1][2] == 'o' or \
     board[2][0] == board[2][1] == board[2][2] == 'o' or \
     board[0][0] == board[1][0] == board[2][0] == 'o' or \
     board[0][1] == board[1][1] == board[2][1] == 'o' or \
     board[0][2] == board[1][2] == board[2][2] == 'o' or \
     board[0][0] == board[1][1] == board[2][2] == 'o' or \
     board[0][2] == board[1][1] == board[2][0] == 'o':
        return True


def unfinished(board: List[List]):
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                return True


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Function which check wins or draw or unfinished game
    :param board: this combination on board
    :type board: List[List]
    """
    if combination_x_winner(board):
        return 'x wins!'
    if combination_o_winner(board):
        return 'o wins!'
    if unfinished(board) is True:
        return 'unfinished!'
    else:
        return 'draw!'

