from homework2.task05 import custom_range

import string

def test_with_one():
    assert custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd',
                                                         'e', 'f']


def test_with_two():
    assert custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i',
                                                              'j', 'k', 'l',
                                                              'm', 'n', 'o']


def test_with_three():
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n',
                                                                  'l', 'j',
                                                                  'h']
