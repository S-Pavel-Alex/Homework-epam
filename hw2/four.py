import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    my_dict = dict()

    @functools.wraps(func)
    def wrapper(*args):
        if args not in my_dict:
            my_dict[args] = func(*args)
        return my_dict[args]
    return wrapper


@cache
def funct(a, b):
    return (a ** b) ** 2
