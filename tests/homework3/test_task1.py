from homework3.task1 import cache


def test_cache():
    invoked = 0

    @cache(time=3)
    def my_function(*args, **kwargs):
        nonlocal invoked
        invoked += 1
        return args, kwargs

    assert invoked == 0
    for _ in range(9):
        assert my_function(3) == ((3,), {})
    assert invoked == 3
