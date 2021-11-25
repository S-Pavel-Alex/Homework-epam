from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """ou need to find a sub-array with length less equal to "k", with
     maximal sum. The written function should return the sum of this
      sub-array."""
    if len(nums) >= k:
        result = nums[:k]
        while nums:
            if sum(result) <= sum(nums[:k]):
                result = nums[:k]
            nums = nums[1:]
        return sum(result)
    else:
        return 0
