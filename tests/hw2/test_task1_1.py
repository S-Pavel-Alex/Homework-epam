import os

from hw2.task01 import count_punctuation_chars

data_folder = os.path.join(os.path.dirname(__file__), 'data')


def test_count_punctuation_char():
    file = os.path.join(data_folder, 'data.txt')
    assert count_punctuation_chars(file) == 4132
