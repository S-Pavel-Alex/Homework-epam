from hw2.task01 import get_most_common_non_ascii_char


def test_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char('data/data.txt') == 'daß'
