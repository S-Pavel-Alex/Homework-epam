import os

from homework2.task1 import get_longest_diverse_words

data_folder = os.path.join(os.path.dirname(__file__), 'data')
file = os.path.join(data_folder, 'data1.txt')


def test_long_words():
    assert get_longest_diverse_words(file) == [
        'unmi\\u00dfverst\\u00e4ndliche', 'Wiederbelebungs\\u00fcbungen',
        'r\\u00e9sistance-Bewegungen,', 'unver\\u00e4u\\u00dferlichen,',
        '\\u00bbWaldg\\u00e4nger\\u00ab', 'Meinungs\\u00e4u\\u00dferung',
        'Werkst\\u00e4ttenlandschaft', 'Souver\\u00e4nit\\u00e4tsan-',
        'Br\\u00fcckenschl\\u00e4gen;', '\\u00bbFreiheitswahl\\u00ab'
    ]
