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


def custom_range(str_ascii, first=None, second=None, third=None):
    try:
        ascii_list = list(str_ascii)
        if second is None and third is None:
            end = ascii_list.index(first)
            return ascii_list[:end]
        elif third is None:
            start = ascii_list.index(first)
            end = ascii_list.index(second)
            return ascii_list[start:end]
        else:
            start = ascii_list.index(first)
            end = ascii_list.index(second)
            return ascii_list[start:end:third]
    except ValueError:
        return 'Non ascii'
