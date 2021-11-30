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
    ascii_list = list(str_ascii)
    if second is None and third is None:
        try:
            end = ascii_list.index(first)
        except ValueError:
            return 'Non ascii'
        return ascii_list[:end]
    elif third is None:
        try:
            start = ascii_list.index(first)
            end = ascii_list.index(second)
        except ValueError:
            return 'Non ascii'
        return ascii_list[start:end]
    else:
        try:
            start = ascii_list.index(first)
            end = ascii_list.index(second)
        except ValueError:
            return 'Non ascii'
        return ascii_list[start:end:third]
