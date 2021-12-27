from homework2.task3 import combinations


def test_correct_example():
    """Test example version"""
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


def test_different_length():
    """Function that take K lists different length"""
    assert combinations([1], [2, 3], [4, 5, 6]) == [
        [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 3, 4], [1, 3, 5], [1, 3, 6]
    ]
