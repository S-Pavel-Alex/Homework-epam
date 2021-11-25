from hw1.four import check_sum_of_four


def test_check_lenght():
    assert check_sum_of_four([1, -2, -3, 3], [-1, -2, -3, -3],
                             [-1, 2, 3, -3], [1, 2, 3, 3]) == 34


def test_all_null():
    assert check_sum_of_four([0, 0, 0, 0], [0, 0, 0, 0],
                             [0, 0, 0, 0], [0, 0, 0, 0]) == 256
