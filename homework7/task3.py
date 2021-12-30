from typing import List
from itertools import chain


def winner_combination(board: List[List]):
    combination = [[board[0][0], board[0][1], board[0][2]],
                   [board[1][0], board[1][1], board[1][2]],
                   [board[2][0], board[2][1], board[2][2]],
                   [board[0][0], board[1][0], board[2][0]],
                   [board[0][1], board[1][1], board[2][1]],
                   [board[0][2], board[1][2], board[2][2]],
                   [board[0][0], board[1][1], board[2][2]],
                   [board[0][2], board[1][1], board[2][0]]]
    for row in combination:
        if row[0] == row[1] == row[2] != '-':
            return row[0]


def unfinished(board: List[List]):
    return '-' in list(chain(*board))


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Function which check wins or draw or unfinished game
    :param board: this combination on board
    :type board: List[List]
    """
    if winner_combination(board) == 'x':
        return 'x wins!'
    if winner_combination(board) == 'o':
        return 'o wins!'
    if unfinished(board):
        return 'unfinished!'
    else:
        return 'draw!'
