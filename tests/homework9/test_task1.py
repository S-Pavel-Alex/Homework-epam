import os

import pytest

from homework9.task1 import merge_sorted_files

file1 = os.path.join(os.path.dirname(__file__), 'file1.txt')
file2 = os.path.join(os.path.dirname(__file__), 'file2.txt')
file3 = os.path.join(os.path.dirname(__file__), 'file3.txt')
file4 = os.path.join(os.path.dirname(__file__), 'file4.txt')
file5 = os.path.join(os.path.dirname(__file__), 'file5.txt')
file6 = os.path.join(os.path.dirname(__file__), 'file6.txt')


@pytest.mark.parametrize("test_input, expected",
                         [
                             ([file1, file2], [1, 2, 3, 4, 6]),
                             ([file3, file2], [2, 4, 6]),
                             ([file5, file2], [2, 4, 6, 10,
                                               50, 60, 1000]),
                             ([file3, file6], []),
                             ([], [])
                         ])
def test_merge_sorted_files_correct_different(test_input, expected):
    assert list(merge_sorted_files(test_input)) == expected
