from homework2.task02 import major_and_minor_elem


def test_correct():
    """Two elements, most common element more n//2"""
    assert major_and_minor_elem([0, 0, 0, 1]) == (0, 1)


def test_if_max_less_():
    """If most common element less than n//2"""
    assert major_and_minor_elem([1, 3, 3, 2, 2, 2, 2, 2, 3, 3, 1, 1]) is None
