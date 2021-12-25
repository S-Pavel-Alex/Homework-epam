from homework7.task3 import tic_tac_toe_checker


def test_x_winner_diagonal():
    assert tic_tac_toe_checker([['-', '-', 'x'],
                                ['-', 'x', 'o'],
                                ['x', 'o', 'x']]) == 'x wins!'


def test_x_winner_row():
    assert tic_tac_toe_checker([['-', 'o', '-'],
                                ['x', 'x', 'x'],
                                ['x', 'o', 'x']]) == 'x wins!'


def test_x_winner_col():
    assert tic_tac_toe_checker([['-', '-', 'x'],
                                ['-', 'o', 'x'],
                                ['x', 'o', 'x']]) == 'x wins!'


def test_o_winner_diagonal():
    assert tic_tac_toe_checker([['o', '-', '-'],
                                ['-', 'o', 'x'],
                                ['x', 'o', 'o']]) == 'o wins!'


def test_o_winner_row():
    assert tic_tac_toe_checker([['-', '-', '-'],
                                ['o', 'o', 'o'],
                                ['x', 'o', 'x']]) == 'o wins!'


def test_o_winner_col():
    assert tic_tac_toe_checker([['o', '-', '-'],
                                ['o', 'x', 'o'],
                                ['o', 'x', 'o']]) == 'o wins!'


def test_unfinished():
    assert tic_tac_toe_checker([['-', '-', '-'],
                                ['x', 'x', 'o'],
                                ['x', 'o', 'o']]) == 'unfinished!'


def test_unfinished_start():
    assert tic_tac_toe_checker([['-', '-', '-'],
                                ['-', '-', '-'],
                                ['-', '-', '-']]) == 'unfinished!'


def test_draw():
    assert tic_tac_toe_checker([['x', 'o', 'o'],
                                ['o', 'x', 'x'],
                                ['o', 'x', 'o']]) == 'draw!'
