import os

from homework1.task03 import find_maximum_and_minimum

data_folder = os.path.join(os.path.dirname(__file__), 'data')


def test_answer_positive():
    """File with two element and they  0"""
    file1 = os.path.join(data_folder, 'file1.txt')
    assert find_maximum_and_minimum(file1) == (0, 0)


def test_file_with_elements_plus_or_minus():
    """Elements positive and negative"""
    file2 = os.path.join(data_folder, 'file2.txt')
    assert find_maximum_and_minimum(file2) == (-125125345, 2151346)


def test_file_with_space():
    """Between elements space"""
    file3 = os.path.join(data_folder, 'file3.txt')
    assert find_maximum_and_minimum(file3) == (-2323, 345)
