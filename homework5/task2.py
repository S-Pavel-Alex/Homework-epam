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
