from homework3.task1 import cache


def test_cache_with_3():
    invoked = 0

    @cache(time=3)
    def my_function(a, b=2):
        nonlocal invoked
        invoked += 1
        return a + b

    assert invoked == 0
    for _ in range(9):
        assert my_function(3) == 5
    assert invoked == 3


def test_cache_with_2():
    invoked = 0

    @cache(time=2)
    def my_function(a, b=2):
        nonlocal invoked
        invoked += 1
        return a + b

    assert invoked == 0
    for _ in range(10):
        assert my_function(3) == 5
    assert invoked == 4
