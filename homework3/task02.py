import time
import struct
import random
import hashlib
import multiprocessing


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def multiprocess_functiion():
    data_number = range(10)
    with multiprocessing.Pool() as pool:
        k = pool.map(slow_calculate, data_number)
    return sum(k)
