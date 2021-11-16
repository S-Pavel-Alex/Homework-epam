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
from typing import Callable

import functools


def cache(func: Callable) -> Callable:
    my_dict = dict()

    @functools.wraps(func)
    def wrapper(*args):
        if args not in my_dict:
            my_dict[args] = func(*args)
        print(my_dict)
        return my_dict[args]
    return wrapper


@cache
def funct(a, b):
    return (a ** b) ** 2


@functools.lru_cache
def functa(a, b):
    return (a ** b) ** 2


some = 100, 2

f1 = funct(*some)
f2 = funct(*some)
print(f1)
print(f2)
print(f1 is f2)
f3 = functa(100, 2)
f4 = functa(100, 2)
print(f3)
print(f4)
print(f3 is f4)
