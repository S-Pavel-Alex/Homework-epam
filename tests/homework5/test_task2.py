import functools

from homework5.task2 import print_result


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_custom_sum_doc():
    """Test positive with function's documentation"""
    assert custom_sum.__doc__ == 'This function can sum any objects' \
                                 ' which have __add___'


def test_custom_sum_name():
    """Test positive with function's name"""
    assert custom_sum.__name__ == 'custom_sum'


def test_not_same():
    assert custom_sum.__original_func(1, 3) == custom_sum(1, 3)
