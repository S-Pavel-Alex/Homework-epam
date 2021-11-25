from homework2.task4 import funct


def test_correct_work():
    some = 100, 2
    val_1 = funct(*some)
    val_2 = funct(*some)

    assert val_1 is val_2
