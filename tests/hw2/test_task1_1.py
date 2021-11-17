import os

from hw2.task01 import (count_punctuation_chars, get_longest_diverse_words,
                        count_non_ascii_chars, get_rarest_char,
                        get_most_common_non_ascii_char)

data_folder = os.path.join(os.path.dirname(__file__), 'data')
file = os.path.join(data_folder, 'data.txt')


def test_count_punctuation_char():
    assert count_punctuation_chars(file) == 4132


def test_long_words():
    assert get_longest_diverse_words(file) == [
        'unmi\\u00dfverst\\u00e4ndliche', 'Wiederbelebungs\\u00fcbungen',
        'r\\u00e9sistance-Bewegungen,', 'unver\\u00e4u\\u00dferlichen,',
        '\\u00bbWaldg\\u00e4nger\\u00ab', 'Meinungs\\u00e4u\\u00dferung',
        'Werkst\\u00e4ttenlandschaft', 'Souver\\u00e4nit\\u00e4tsan-',
        'Br\\u00fcckenschl\\u00e4gen;', '\\u00bbFreiheitswahl\\u00ab'
    ]


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(file) == 2971


def test_rerest_char():
    assert get_rarest_char(file) == ")"


def test_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(file) == 'daß'
