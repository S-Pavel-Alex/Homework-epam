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
    total = 0
    lenth = len(a)
    my_dict = {}
    for i in range(lenth):
        for j in range(lenth):
            positive_sum = a[i] + b[j]
            if positive_sum in my_dict:
                my_dict[positive_sum] += 1
            else:
                my_dict[positive_sum] = 1

    for i in range(lenth):
        for j in range(lenth):
            negative_sum = -(c[i] + d[j])
            if negative_sum in my_dict:
                total += my_dict[negative_sum]
    return total
