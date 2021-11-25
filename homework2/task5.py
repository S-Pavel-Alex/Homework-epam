"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd',
'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l',
 'j', 'h']

"""


def custom_range(f, *some):
    my_some_list = [*some]
    ascii_list = list(f)
    lenth = len(my_some_list)
    if lenth == 1:
        fin = ascii_list.index(my_some_list[0])
        return ascii_list[:fin]
    elif lenth == 2:
        start = ascii_list.index(my_some_list[0])
        fin = ascii_list.index(my_some_list[1])
        return ascii_list[start:fin]
    elif lenth == 3:
        start = ascii_list.index(my_some_list[0])
        fin = ascii_list.index(my_some_list[1])
        step = my_some_list[2]
        return ascii_list[start:fin:step]
