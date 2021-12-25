from typing import List


class Board:
    def __init__(self, board: List[List]):
        self.board = board

    def check_winner_in_row(self) -> str or bool:
        """Method which checking if win in row combination"""
        for row in self.board:
            if row[0] == row[1] == row[2] == 'x':
                return 'x'
            elif row[0] == row[1] == row[2] == 'o':
                return 'o'
        return False

    def check_winner_in_diagonal(self) -> str or bool:
        """Method which checking if win in diagonal combination"""
        a0, c0 = self.board[0][0], self.board[0][2]
        b1 = self.board[1][1]
        a2, c2 = self.board[2][0], self.board[2][2]
        if a0 == b1 == c2 == 'x' or c0 == b1 == a2 == 'x':
            return 'x'
        elif a0 == b1 == c2 == 'o' or c0 == b1 == a2 == 'x':
            return 'o'
        return False

    def check_winner_col(self) -> str or bool:
        """Method which checking if win in column combination"""
        a0, b0, c0 = self.board[0][0], self.board[0][1], self.board[0][2]
        a1, b1, c1 = self.board[1][0], self.board[1][1], self.board[1][2]
        a2, b2, c2 = self.board[2][0], self.board[2][1], self.board[2][2]
        if a0 == a1 == a2 == 'x' != '-' or \
                b0 == b1 == b2 == 'x' or \
                c0 == c1 == c2 == 'x':
            return 'x'
        elif a0 == a1 == a2 == 'o' or \
                b0 == b1 == b2 == 'o' or \
                c0 == c1 == c2 == 'o':
            return 'o'
        return False

    def check_unfinished(self) -> bool:
        """Method checking unfinished game"""
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '-':
                    return True
        return False


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Function which check wins or draw or unfinished game
    :param board: this combination on board
    :type board: List[List]
    """
    board = Board(board)
    if board.check_winner_in_row() == 'x':
        return 'x wins!'
    elif board.check_winner_in_row() == 'o':
        return 'o wins!'
    else:
        if board.check_winner_in_diagonal() == 'x':
            return 'x wins!'
        elif board.check_winner_in_diagonal() == 'o':
            return 'o wins!'
        else:
            if board.check_winner_col() == 'x':
                return 'x wins!'
            elif board.check_winner_col() == 'o':
                return 'o wins!'
            else:
                if board.check_unfinished():
                    return 'unfinished!'
                else:
                    return 'draw!'
