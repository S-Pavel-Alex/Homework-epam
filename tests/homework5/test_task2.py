import functools

from homework5.task2 import saver_decorator


def print_result_plus_1(func):
    @saver_decorator(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result + 1
    return wrapper


@print_result_plus_1
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
    """Test show origin function answer is not answer cover function """
    assert (custom_sum.__original_func(1, 3) + 1) == custom_sum(1, 3)
