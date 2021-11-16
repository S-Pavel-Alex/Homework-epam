from homework2.task02 import major_and_minor_elem


def test_two_elemenrs():
    assert major_and_minor_elem([0, 0, 0, 1]) == (0, 1)


def test_four_elements():
    assert major_and_minor_elem([1, 0, 0, 2, 2, 2, 2, 2, 3])