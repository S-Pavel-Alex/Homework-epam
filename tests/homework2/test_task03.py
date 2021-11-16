from homework2.task3 import combinat


def test_correct_example():
    """Test example version"""
    assert combinat([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]
