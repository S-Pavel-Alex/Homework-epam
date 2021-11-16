from homework2.task01 import get_longest_diverse_words, get_rarest_char
from homework2.task01 import count_punctuation_chars, count_non_ascii_chars
from homework2.task01 import get_most_common_non_ascii_char

answer = ['unmi\\u00dfverst\\u00e4ndliche', 'r\\u00e9sistance-Bewegungen,',
          'Wiederbelebungs\\u00fcbungen', '\\u00bbWaldg\\u00e4nger\\u00ab',
          'unver\\u00e4u\\u00dferlichen,', 'Souver\\u00e4nit\\u00e4tsan-',
          'Werkst\\u00e4ttenlandschaft', 'Br\\u00fcckenschl\\u00e4gen;',
          'Meinungs\\u00e4u\\u00dferung', 'Millionenbev\\u00f6lkerung']
text = 'data.txt'


def check_long_words():
    assert get_longest_diverse_words(text) == answer


def chech_rerest_char():
    assert get_rarest_char(text) == ")"


def check_count_punctuation_char():
    assert count_punctuation_chars(text) == 4132


def check_count_non_ascii_chars():
    assert count_non_ascii_chars(text) == 2971


def check_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(text) == 'daß'
