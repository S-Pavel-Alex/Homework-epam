"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from inspect import signature
from typing import Callable


def cache(func: Callable) -> Callable:
    my_dict = dict()

    def wrapper(*args, **kwargs):
        sig = signature(func)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        arg = bound.arguments['args']
        kwarg = bound.arguments['kwargs']
        key = str((arg, kwarg))
        if key not in my_dict:
            my_dict[key] = func(*arg, **kwarg)
        return my_dict[key]
    return wrapper
