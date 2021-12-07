from homework4.task1 import read_magic_number


def test_positive_inside_range(open_correct_file_with_correct_item):
    """This test show positive result for element
    in range [1, 3)"""
    assert read_magic_number('temp.txt') is True


def test_negative_inside_range(open_file_with_incorrect_item):
    """This test show negative result for element
    in range [1, 3)"""
    assert read_magic_number('temp.txt') is False
