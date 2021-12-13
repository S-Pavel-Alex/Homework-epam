import pytest

from homework5.task2 import custom_sum


def test_custom_sum_doc():
    """Test positive with function's documentation"""
    assert custom_sum.__doc__ == 'This function can sum any objects' \
                                 ' which have __add___'


def test_custom_sum_name():
    """Test positive with function's name"""
    assert custom_sum.__name__ == 'custom_sum'


@pytest.mark.parametrize(
    "args, result",
    [
        ((1, 2, 3, 4), 10),
        (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
    ]
)
def test_result_print(args, result):
    assert custom_sum(*args) == result
