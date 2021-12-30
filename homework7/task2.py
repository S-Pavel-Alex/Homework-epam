from itertools import zip_longest


def generation(string):
    total = 0
    for item in string:
        if item == '#':
            total += 1
            continue
        if total > 0:
            total -= 1
            continue
        else:
            yield item


def backspace_compare(first: str, second: str) -> bool:
    for one, two in zip_longest(generation(first[::-1]),
                                generation(second[::-1])):
        if one != two:
            return False
    return True
