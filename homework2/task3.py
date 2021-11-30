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
import itertools
from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    return list(map(lambda x: list(x), [x for x in itertools.product(*args)]))



print(combinations([2, 3]))
# # print(list(product([1, 2], [3, 4])))
#
# def product2345(*args):
#     # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
#     # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
#     pools = [tuple(pool) for pool in args]
#     result = [[]]
#     for pool in pools:
#         result = [x+[y] for x in result for y in pool]
#     for prod in result:
#         yield tuple(prod)
#     return result
#
# # print(list(product2345([1, 2], [3, 4])))