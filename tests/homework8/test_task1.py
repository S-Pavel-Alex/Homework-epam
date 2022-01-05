import os

import pytest

from homework8.task1 import KeyValueStorage

file1 = os.path.join(os.path.dirname(__file__), "task1.txt")
file_error = os.path.join(os.path.dirname(__file__), "task_error.txt")

K = KeyValueStorage(file1)


def test_name_correct():
    assert K.name == 'kek'
    assert K['name'] == 'kek'


def test_last_name_correct():
    assert K.last_name == 'top'
    assert K['last_name'] == 'top'


def test_power_correct():
    assert K.power == '9001'
    assert K['power'] == '9001'


def test_song_correct():
    assert K.song == 'shadilay'
    assert K['song'] == 'shadilay'


def test_no_file():
    with pytest.raises(FileNotFoundError) as er:
        KeyValueStorage('no_task.txt')
    assert str(er.value) == 'File no_task.txt not founded'


def test_bad_key():
    with pytest.raises(ValueError) as er:
        KeyValueStorage(file_error)
    assert str(er.value) == '1 is bad key'
