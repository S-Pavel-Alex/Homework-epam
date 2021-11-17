from hw2.task01 import count_punctuation_chars


def test_count_punctuation_char():
    assert count_punctuation_chars('data.txt') == 4132
