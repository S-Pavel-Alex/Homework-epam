"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a
    Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    assert len(data) >= 3
    assert data[0] == 0
    assert data[1] == data[2] == 1
    a, b, c = data[0], data[1], data[2]

    while data:
        if not _check_window(a, b, c):
            raise ValueError("Invalid data")
        try:
            a, b, c = b, c, data[3]
        except IndexError:
            break
        data = data[1:]
    return True


# print(check_fibonacci([5, 6, 11]))
print(check_fibonacci([0, 0, 1]))
print(print(check_fibonacci([0, 1, 1, 2, 3, 5, 9, 14])))