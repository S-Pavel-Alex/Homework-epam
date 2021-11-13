from homework2.task02 import major_and_minor_elem


def test_positive():
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_positive2():
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


#def test_with_null():
    #assert major_and_minor_elem([0, 0, 0, 1]) == (0, 1)


def test_with_minus():
    assert major_and_minor_elem([-2, -2, -2, 5, 5]) == (-2, 5)
