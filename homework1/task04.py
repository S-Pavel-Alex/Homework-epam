"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] +
    + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    n = len(a)
    total = 0
    for i in range(n):
        for j in range(n):
            if a[i] + b[j] == 0:
                total += 1
    count = 0
    for i in range(len(c)):
        for j in range(len(d)):
            if c[i] + d[j] == 0:
                count += 1
    return total + count


print(check_sum_of_four([2, 4, 6], [2, 4, -6],
                        [2, -4, -6], [2, 4, -6]))