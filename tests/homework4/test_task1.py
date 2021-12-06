from homework4 import *


def test_positive_inside_range(read_magic_number):
    """This test show positive resault for element
    in range [1, 3)"""
    assert read_magic_number('a') is True