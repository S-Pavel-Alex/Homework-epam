from homework2.task2 import major_and_minor_elem


def test_correct_with_0_and_positive_items():
    """Two elements positive and 0"""
    assert major_and_minor_elem([0, 0, 0, 1]) == (0, 1)


def test_correct_with_different():
    """Test with different items"""
    assert major_and_minor_elem([1, 2, 2, 3, 3, 4, 4, 4]) == (4, 1)


def test_correct_with_negative_item():
    """If items negative"""
    assert major_and_minor_elem([-1, -1, 2]) == (-1, 2)
