from homework1.task03 import find_maximum_and_minimum


def test_answer_positive():
    """File with two element and they 0"""
    assert find_maximum_and_minimum('a.txt') == (0, 0)


def test_file_with_elements_plus_or_minus():
    """Elements positive and negative"""
    assert find_maximum_and_minimum('b.txt') == (-125125345, 2151346)


def test_file_with_space():
    """Between elements space"""
    assert find_maximum_and_minimum('c.txt') == (-2323, 345)
