import os

import pytest

from homework8.task2 import TableData

bd = os.path.join(os.path.dirname(__file__), "example.sqlite")

PRESIDENTS = TableData(bd, 'presidents')
BOOKS = TableData(bd, 'books')


@pytest.mark.parametrize('test_input, expected',
                         [
                             (PRESIDENTS, 3),
                             (BOOKS, 3)
                         ])
def test_table_data_len(test_input, expected):
    """How many row in table"""
    assert len(test_input) == expected


def test_table_data_row_presidents_correct():
    """All row about name for presidents table"""
    assert PRESIDENTS['Trump'] == ('Trump', 1337, 'US')


def test_table_data_row_presidents_negative():
    """If name not presidents table"""
    with pytest.raises(TypeError):
        PRESIDENTS['Putin']


def test_table_data_row_books():
    """All row about name for books table"""
    assert BOOKS['1984'] == ('1984', 'Orwell')


def test_table_data_row_books_negative():
    """If name not book table"""
    with pytest.raises(TypeError):
        BOOKS['Harry Potter']


def test_table_data_into_correct():
    """If name in presidents table"""
    assert ("Yeltsin" in PRESIDENTS) is True


def test_table_data_into_presidents():
    """If name in books table"""
    assert ("1984" in BOOKS) is True


def test_iterator_president():
    """Test iterator for presidents"""
    for president in PRESIDENTS:
        assert president['name'] in [
            president['name'] for president in PRESIDENTS
        ]


def test_iterator_books():
    """Test iterator for books"""
    for book in BOOKS:
        assert book['name'] in [
            book['name'] for book in BOOKS
        ]
