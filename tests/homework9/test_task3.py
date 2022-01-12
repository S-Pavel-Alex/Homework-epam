import os
from pathlib import Path

from homework9.task3 import universal_file_counter

file_extension = "txt"
test_dir = Path(os.path.dirname(__file__), 'dir')
tokenizer = str.split


def test_count_lines():
    """Testing that without tokenizer function returns sum of number of
     lines in all files with specified file extension from directory."""
    assert universal_file_counter(test_dir, file_extension) == 6


def test_count_with_tokenizer():
    """Testing that with tokenizer function returns sum of number of
     lines in all files with specified file extension from directory."""
    assert universal_file_counter(test_dir, file_extension, tokenizer) == 10
