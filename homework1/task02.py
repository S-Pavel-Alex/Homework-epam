"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a
    Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    """Check sum"""
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) >= 3:
        if data[0] == 0:
            if data[1] == data[2] == 1:
                a, b, c = data[0], data[1], data[2]

                while data:
                    if not _check_window(a, b, c):
                        return False
                    try:
                        a, b, c = b, c, data[3]
                    except IndexError:
                        break
                    data = data[1:]
            else:
                return False
        else:
            return False
    else:
        return False
    return True
