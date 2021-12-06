from inspect import signature


def cache(time):
    def odder(func):
        my_dict = dict()

        def wrapper(*args, **kwargs):
            sig = signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            key = str(bound)
            if key in my_dict and my_dict[key][1] != 0:
                my_dict[key][1] -= 1
                return my_dict[key][0]
            else:
                my_dict[key] = [func(*args, **kwargs), time]
                my_dict[key][1] -= 1
                return my_dict[key][0]
        return wrapper
    return odder
