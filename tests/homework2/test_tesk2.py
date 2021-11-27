from homework2.task2 import major_and_minor_elem


def test_correct():
    """Two elements, most common element more n//2"""
    assert major_and_minor_elem([0, 0, 0, 1]) == (0, 1)
