from hw2.task01 import count_punctuation_chars

text = 'data.txt'


def test_count_punctuation_char():
    assert count_punctuation_chars(text) == 4132
