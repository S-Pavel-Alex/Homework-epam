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
    """
    Decorator which save doc, name, original function
    :param source_func: original function
    """
    def a_decorator(recipient_function):
        recipient_function.__name__ = source_func.__name__
        recipient_function.__doc__ = source_func.__doc__
        setattr(recipient_function, '__original_func', source_func)
        return recipient_function
    return a_decorator


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
