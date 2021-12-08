import pytest

from homework4.task1 import read_magic_number


def test_positive_inside_range(open_correct_file_with_correct_item):
    """This test show positive result for element
    in range [1, 3)"""
    assert read_magic_number('temp.txt') is True


def test_negative_inside_range(open_file_with_incorrect_item):
    """This test show negative result for element
    in range [1, 3)"""
    assert read_magic_number('temp.txt') is False


def test_negative_with_item_str(open_file_item_str):
    """This test show negative result for element
    in range [1, 3) if item is string"""
    with pytest.raises(ValueError):
        read_magic_number('temp.txt')


def test_negative_if_no_file(open_file_item_str):
    """This test show negative result for element
    in range [1, 3) if file is no"""
    with pytest.raises(ValueError):
        read_magic_number('no_file.txt')


def test_file_is_empty(open_file_is_empty):
    """This test show negative result for element
    in range [1, 3) if file is empty"""
    with pytest.raises(ValueError):
        read_magic_number('temp.txt')


def test_file_has_2_string(open_file_has_2_string):
    """This test show negative result for element
    in range [1, 3) if file has 2 string"""
    assert read_magic_number('temp.txt') is True
