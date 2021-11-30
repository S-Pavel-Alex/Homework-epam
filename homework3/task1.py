import functools


def cache(time):
    def oder(func):
        my_dict = dict()

        @functools.wraps(func)
        def wrapper(*args):
            if args not in my_dict:
                my_dict[args] = func(*args)
            return my_dict[args]
        return wrapper
    return oder


total = 0


@cache(time=3)
def my_fun(item):
    global total
    total += 1
    return item, total
