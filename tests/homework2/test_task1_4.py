import os

from homework2.task1 import get_rarest_char

data_folder = os.path.join(os.path.dirname(__file__), 'data')
file = os.path.join(data_folder, 'data1.txt')


def test_rerest_char():
    assert get_rarest_char(file) == "›"
