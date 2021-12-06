from inspect import signature


def cache(time):
    def odder(func):
        my_dict = dict()

        def wrapper(*args, **kwargs):
            sig = signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            key = str(bound)
            if key not in my_dict:
                my_dict[key] = [func(*args, **kwargs), time]
                my_dict[key][1] -= 1
                return my_dict[key][0]
            elif key in my_dict and my_dict[key][1] != 0:
                my_dict[key][1] -= 1
                return my_dict[key][0]
            else:
                del my_dict[key]
                my_dict[key] = [func(*args, **kwargs), time]
                my_dict[key][1] -= 1
                return my_dict[key][0]
        return wrapper
    return odder
