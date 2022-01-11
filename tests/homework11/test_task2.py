from homework11.task2 import ElderDiscount, MorningDiscount, Oder


def test_without_discount():
    """Without discount"""
    oder = Oder(100)
    assert oder.final_price() == 100


def test_morning_discount():
    """With morning discount"""
    oder = Oder(100, MorningDiscount())
    assert oder.final_price() == 75


def test_elder_discount():
    """With elder discount"""
    oder = Oder(100, ElderDiscount())
    assert oder.final_price() == 20
