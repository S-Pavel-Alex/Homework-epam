import time

from homework3.task02 import slow_calculate


def test_slow_calculation():
    start = time.time()
    for i in range(500):
        slow_calculate(i)
    assert time.time() - start <= 60
