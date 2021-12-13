import unittest.mock

import pytest

from homework4.task2 import count_dots_on_i


def test_count_dots_on_i_positive():
    assert count_dots_on_i('https://example.com/') == 59


def test_mock_count_dots_on_i_positive():
    with unittest.mock.patch('requests.get') as mock_ob:
        mock_ob().text = 'i'
        assert count_dots_on_i('https://example.com/') == 1


def test_mock_count_dots_without_i_positive():
    with unittest.mock.patch('requests.get') as mock_ob:
        mock_ob().text = 'not'
        assert count_dots_on_i('https://example.com/') == 0


def test_mock_count_dots_without_text_positive():
    with unittest.mock.patch('requests.get') as mock_ob:
        mock_ob().text = ''
        assert count_dots_on_i('https://example.com/') == 0


def test_count_dots_incorrect_url():
    with pytest.raises(ValueError):
        count_dots_on_i('https://sefgg.com/')
