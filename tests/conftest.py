import os

import pytest


@pytest.fixture()
def open_correct_file_with_correct_item():
    with open('temp.txt', 'w') as file:
        file.write('2')
    yield
    os.remove('temp.txt')


@pytest.fixture()
def open_file_with_incorrect_item():
    with open('temp.txt', 'w') as file:
        file.write('4.5')
    yield
    os.remove('temp.txt')
