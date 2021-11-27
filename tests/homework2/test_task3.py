from homework2.task3 import combinat


def test_correct_example():
    """Test example version"""
    assert combinat([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


def test_different_length():
    """Function that take K lists different length"""
    assert combinat([1], [2, 3], [4, 5, 6]) == [
        [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 3, 4], [1, 3, 5],
        [1, 3, 6], [1, 4, 5], [1, 4, 6], [1, 5, 6], [2, 3, 4], [2, 3, 5],
        [2, 3, 6], [2, 4, 5], [2, 4, 6], [2, 5, 6], [3, 4, 5], [3, 4, 6],
        [3, 5, 6]
    ]


def test_one_list():
    """Function that take K = 1 lists"""
    assert combinat([2, 3]) == [2, 3]
