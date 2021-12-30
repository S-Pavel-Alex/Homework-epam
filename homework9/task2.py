import contextlib


class Context:
    def __init__(self, exception: type(Exception)):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.exception is exc_type:
            return True


@contextlib.contextmanager
def cont_manager(exception: type(Exception)):
    try:
        yield
    except exception:
        pass
