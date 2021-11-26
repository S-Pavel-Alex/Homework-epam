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


if __name__ == '__main__':
    data_number = range(500)
    with multiprocessing.Pool(2) as pool:
        pool.map(slow_calculate, data_number)
