import os

from homework4.task01 import read_magic_number
data_folder = os.path.join(os.path.dirname(__file__), 'data')


def test_positive_inside_range():
    """This test show positive resault for element
    in range [1, 3)"""
    file1 = os.path.join(data_folder, 'file_positive.txt')
    assert read_magic_number(file1) is True


def test_positive_first_border():
    """Test positive if element in border  is 1"""
    file2 = os.path.join(data_folder, 'file_positive_border.txt')
    assert read_magic_number(file2) is True


def test_negative_outside_range():
    """Negative test. If item not in range"""
    file3 = os.path.join(data_folder, 'file_negative_test.txt')
    assert read_magic_number(file3) is False


def test_value_error():
    """If in file not item"""
    file4 = os.path.join(data_folder, 'file_value_error.txt')
    assert read_magic_number(file4) is False


def test_no_file():
    """If file for reading is none"""
    assert read_magic_number('file_is_none.txt') is False
