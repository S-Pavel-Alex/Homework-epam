"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List

nu = [1, 3, -1, -3, 5, 3, 6, 7]
ki = 3


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    nums.sort()
    nums.reverse()
    nums = nums[0:k]
    result = sum(nums)
    return result


print(find_maximal_subarray_sum(nu, ki))
