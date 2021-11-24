import sys

from homework4.task03 import my_precious_logger


def test_stderr_write_positive():
    assert my_precious_logger('error') is sys.stderr.write('error')


def test_stderr_write_negative():
    assert my_precious_logger('test') is not sys.stderr.write('test')


def test_stdout_write_positive():
    assert my_precious_logger('test') is sys.stdout.write('test')
