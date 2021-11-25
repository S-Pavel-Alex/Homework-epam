import os

from homework2.task1 import count_punctuation_chars

data_folder = os.path.join(os.path.dirname(__file__), 'data')
file = os.path.join(data_folder, 'data1.txt')


def test_count_punctuation_char():
    assert count_punctuation_chars(file) == 4132
