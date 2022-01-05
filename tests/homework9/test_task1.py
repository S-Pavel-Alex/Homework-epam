import pytest

from homework9.task1 import merge_sorted_files


@pytest.mark.parametrize("test_input, expected",
                         [
                             (['file1.txt', 'file2.txt'], [1, 2, 3, 4, 6]),
                             (['file3.txt', 'file2.txt'], [2, 4, 6]),
                             (['file4.txt', 'file2.txt'], [-5, -1, 2, 4, 6]),
                             (['file5.txt', 'file2.txt'], [2, 4, 6, 10,
                                                           50, 60, 1000]),
                             (['file3.txt', 'file6.txt'], []),
                             (['file1.txt', 'file2.txt', 'file4.txt'],
                              [-5, -1, 1, 2, 3, 4, 6]),
                             ([], [])
                         ])
def test_merge_sorted_files_correct_different(test_input, expected):
    assert merge_sorted_files(test_input) == expected
