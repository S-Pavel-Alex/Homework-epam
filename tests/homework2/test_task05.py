from homework2.task05 import custom_range

import string


def test_with_one():
    """With one argument is stop"""
    assert custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd',
                                                         'e', 'f']


def test_with_two():
    """Two arguments are start and stop"""
    assert custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i',
                                                              'j', 'k', 'l',
                                                              'm', 'n', 'o']


def test_with_three():
    """Three argumets are start, stop and step"""
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n',
                                                                  'l', 'j',
                                                                  'h']
