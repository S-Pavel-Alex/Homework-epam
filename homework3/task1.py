import functools


def cache(time):
    def odder(func):
        my_dict = dict()
        def wrapper(*args, **kwargs):
            total = time
            key = str((args, kwargs))
            if key not in my_dict:
                my_dict[key] = [func(*args, **kwargs), total]

            return my_dict[key]
        return wrapper
    return odder


@cache(time=3)
def my_function(*args, **kwargs):
    return args, kwargs

print(my_function(1, 3))