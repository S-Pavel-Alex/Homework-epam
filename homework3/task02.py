import hashlib
import multiprocessing
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def multiprocess_function():
    data_number = range(500)
    with multiprocessing.Pool(60) as pool:
        k = pool.map(slow_calculate, data_number)
    return sum(k)
