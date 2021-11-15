"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any

from itertools import combinations


def combinat(*args: List[Any]) -> List[List]:
    a = []
    ar_len = len(args)
    for i in range(ar_len):
        a += args[i]
    combo = list(combinations(a, ar_len))
    finish = list(map(lambda x: list(x), combo))
    return finish
