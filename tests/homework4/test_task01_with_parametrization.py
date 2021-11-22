import os
import pytest

from homework4.task01 import read_magic_number
data_folder = os.path.join(os.path.dirname(__file__), 'data')
file1 = os.path.join(data_folder, 'file_positive.txt')
file2 = os.path.join(data_folder, 'file_positive_border.txt')
file3 = os.path.join(data_folder, 'file_negative_test.txt')
file4 = os.path.join(data_folder, 'file_value_error.txt')

test_data = [
    (file1, True),
    (file2, True),
    (file3, False),
    (file4, False),
    ('file_is_none.txt', False)
]


@pytest.mark.parametrize("test_input,expected", test_data)
def test_read_text_for_range(test_input, expected):
    assert read_magic_number(test_input) is expected



