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


def multi_fuction():
    data_number = range(5)
    with multiprocessing.Pool(2) as pool:
        list_with_sum = pool.map(slow_calculate, data_number)
    return sum(list_with_sum)


print(multi_fuction())