from homework3.task1 import my_fun


def test_cache():
    assert my_fun(1) == (1, 1)
    assert my_fun(1) == (1, 1)
    assert my_fun(1) == (1, 1)
    assert my_fun(2) == (2, 2)
    assert my_fun(2) == (2, 2)
    assert my_fun(2) == (2, 2)
