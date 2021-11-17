from hw2.task01 import (count_punctuation_chars, count_non_ascii_chars,
                        get_longest_diverse_words, get_rarest_char,
                        get_most_common_non_ascii_char)


def test_long_words():
    assert get_longest_diverse_words('data.txt') == [
        'unmi\\u00dfverst\\u00e4ndliche', 'Wiederbelebungs\\u00fcbungen',
        'r\\u00e9sistance-Bewegungen,', 'unver\\u00e4u\\u00dferlichen,',
        '\\u00bbWaldg\\u00e4nger\\u00ab', 'Meinungs\\u00e4u\\u00dferung',
        'Werkst\\u00e4ttenlandschaft', 'Souver\\u00e4nit\\u00e4tsan-',
        'Br\\u00fcckenschl\\u00e4gen;', '\\u00bbFreiheitswahl\\u00ab'
    ]


def test_rerest_char():
    assert get_rarest_char('data.txt') == ")"


def test_count_punctuation_char():
    assert count_punctuation_chars('data.txt') == 4132


def test_count_non_ascii_chars():
    assert count_non_ascii_chars('data.txt') == 2971


def test_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char('data.txt') == 'daß'
