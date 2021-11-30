import time

from homework3.task02 import multi_fuction


def test_slow_calculation():
    start = time.time()
    multi_fuction()
    assert time.time() - start <= 60
