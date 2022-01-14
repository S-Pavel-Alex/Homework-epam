from homework11.task2 import Oder


def morning_discount(order: Oder) -> float:
    if order.price < 5000:
        return 0.4 * order.price
    return 0.5 * order.price


def elder_discount(order: Oder) -> float:
    if order.price < 5000:
        return 0.1 * order.price
    return 0.2 * order.price


def test_without_discount():
    """Without discount"""
    oder = Oder(100)
    assert oder.final_price() == 100


def test_morning_discount_less():
    """With morning discount less 5000"""
    oder = Oder(100, morning_discount)
    assert oder.final_price() == 60


def test_morning_discount_high():
    """With morning discount high  5000"""
    oder = Oder(10000, morning_discount)
    assert oder.final_price() == 5000


def test_elder_discount_less():
    """With elder discount less 5000"""
    oder = Oder(100, elder_discount)
    assert oder.final_price() == 90


def test_elder_discount_high():
    """With morning discount high  5000"""
    oder = Oder(10000, elder_discount)
    assert oder.final_price() == 8000
