from homework1.task03 import find_maximum_and_minimum

import os

data_folder = os.path.join(os.path.dirname(__file__), 'data')

def test_answer_positive():
    """File with two element and they  0"""
    file1 = os.path.join(data_folder, 'file1.txt')
    assert find_maximum_and_minimum(file1) == (0, 0)


# def test_file_with_elements_plus_or_minus():
#     """Elements positive and negative"""
#     assert find_maximum_and_minimum(Homework-epam\tests\homework1\data\file1.txt) \
#            == (-125125345, 2151346)
#
#
# def test_file_with_space():
#     """Between elements space"""
#     assert find_maximum_and_minimum('C:\\Users\\forxb\\Documents\\home'
#                                     'work\\Homework-epam\\home'
#                                     'work1\\file3.txt') == (-2323, 345)
