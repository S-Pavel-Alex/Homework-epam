from hw2.task01 import get_rarest_char


def test_rerest_char():
    assert get_rarest_char( 'data/data.txt' ) == ")"
