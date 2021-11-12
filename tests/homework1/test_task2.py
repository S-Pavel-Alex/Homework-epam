from homework1.task02 import _check_window, check_fibonacci


def test_check_sum_true():
    """Sum first and second elements it's third True"""
    assert _check_window(1, 2, 3)


def test_check_sum_false():
    """Sum first and second elements it's third it's False"""
    assert not _check_window(2, 2, 3)


def test_check_fib_three_elements():
    """Three elements:
    First element 0
    Second and third 1"""
    assert check_fibonacci([0, 1, 1])
