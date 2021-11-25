import os

from hw2.one import count_non_ascii_chars

data_folder = os.path.join(os.path.dirname(__file__), 'data')
file = os.path.join(data_folder, 'data1.txt')


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(file) == 2971
