import os

from hw2.task01 import get_most_common_non_ascii_char

data_folder = os.path.join(os.path.dirname(__file__), 'data')
file = os.path.join(data_folder, 'data.txt')


def test_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(file) == 'daß'
