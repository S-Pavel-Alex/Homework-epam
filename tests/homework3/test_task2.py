import time

from homework3.task02 import slow_calculate


def test_slow_calculation():
    start = time.time()
    slow_calculate(500)
    assert time.time() - start <= 60
