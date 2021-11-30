from homework3.task4 import is_armstrong


def test_is_armstrong_positive():
    assert is_armstrong(153) is True


def test_is_armstrong_negative():
    assert is_armstrong(10) is False


def test_is_armstrong_negative_with_number_less_0():
    assert is_armstrong(0) is False
