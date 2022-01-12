from homework9.task2 import Context, cont_manager


def test_context_index():
    i = []
    with Context(IndexError):
        i[1]


def test_cont_manager_index():
    i = []
    with cont_manager(IndexError):
        i[1]


def test_context_zero():
    with Context(ZeroDivisionError):
        1/0


def test_cont_manager_zero():
    with cont_manager(ZeroDivisionError):
        1/0
