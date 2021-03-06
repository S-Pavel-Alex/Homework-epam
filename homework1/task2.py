"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a
    Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_window(x: int, y: int, z: int) -> bool:
    """Check sum"""
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    if not len(data) >= 3:
        return False
    if not data[0] == 0:
        return False
    if not data[1] == data[2] == 1:
        return False
    a, b, c = data[0], data[1], data[2]

    while data:
        if not check_window(a, b, c):
            try:
                a, b, c = b, c, data[3]
            except IndexError:
                break
        data = data[1:]
    return True
