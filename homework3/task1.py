from inspect import signature


def cache(time):
    def odder(func):
        my_dict = dict()
        total = time
        wrapper.count = 0
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            sig = signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            arg = bound.arguments['args']
            kwarg = bound.arguments['kwargs']
            key = str((arg, kwarg))
            nonlocal total
            if key not in my_dict:
                total -= 1
                my_dict[key] = [func(*arg, **kwarg), total]
                return my_dict[key][0]
            else:
                if total != 0:
                    total -= 1
                    return my_dict[key][0]
                else:
                    del my_dict[key]

        return wrapper
    return odder
