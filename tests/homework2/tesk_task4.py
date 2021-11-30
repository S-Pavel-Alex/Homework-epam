from homework2.task4 import my_function


def test_correct_work():
    some = 100, 2
    val_1 = my_function(*some)
    val_2 = my_function(*some)
    assert val_1 is val_2


def test_correct_work_with_unhashable():
    val_1 = my_function(1, [2], c=2, d=2)
    val_2 = my_function(1, [2], c=2, d=2)
    assert val_1 is val_2
