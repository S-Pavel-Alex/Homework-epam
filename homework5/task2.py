import functools


def print_result(func):
    @saver_decorator(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


def saver_decorator(source_func):
    def a_decorator(recipient_function):
        def wrapper(*args, **kwargs):
            wrapper.__name__ = source_func.__name__
            wrapper.__doc__ = source_func.__doc__
            setattr(wrapper, '__original_func', source_func)
            return recipient_function(*args, **kwargs)
        return wrapper
    return a_decorator


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)
    print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
    print(custom_sum.__name__)  # 'custom_sum'
    print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)
