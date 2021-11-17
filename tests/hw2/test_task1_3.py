from hw2.task01 import count_non_ascii_chars


def test_count_non_ascii_chars():
    assert count_non_ascii_chars('data/data.txt') == 2971
