import urllib.request

from homework4.task02 import count_dots_on_i


def test_count_dots_on_i_positive():
    """In dots https://example.com/ must be 59 i"""
    assert count_dots_on_i('https://example.com/') == 59


def test_count_dots_on_i_negative():
    """In dots https://example.com/ must be 59 i"""
    assert count_dots_on_i('https://example.com/') != 5


def test_connect():
    """Test connect https://example.com/"""
    assert urllib.request.urlopen('https://example.com/').getcode() == 200
