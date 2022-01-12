import contextlib


class Context:
    """Class context manager for exception"""
    def __init__(self, exception: Exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.exception is exc_type


@contextlib.contextmanager
def cont_manager(exception: Exception):
    """Generation context manager for exception"""
    try:
        yield
    except exception:
        pass
