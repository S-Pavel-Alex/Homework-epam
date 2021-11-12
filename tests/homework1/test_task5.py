from homework1.task05 import find_maximal_subarray_sum


def test_positive():
    """Correct working"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_negative():
    """If len < k"""
    assert find_maximal_subarray_sum([1], 2) == 0


def test_negative_with_null_elements():
    """If the list is empty"""
    assert find_maximal_subarray_sum([], 1) == 0
