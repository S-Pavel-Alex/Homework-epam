import os

from homework2.task1 import get_longest_diverse_words

data_folder = os.path.join(os.path.dirname(__file__), 'data')
file = os.path.join(data_folder, 'data1.txt')


def test_long_words():
    assert get_longest_diverse_words(file) == [
        'politisch-strategischen', 'Verfassungsverletzungen',
        'Geschichtsphilosophie.', 'zoologisch-politischen',
        'Wiederbelebungsübungen', 'résistance-Bewegungen,',
        'Entscheidungsschlacht.', 'Werkstättenlandschaft',
        'Gewissenserforschung,', 'politisch-technischen'
    ]
