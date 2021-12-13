from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Function takes number N and return list with N FizzBuzz numbers
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(3)
    ['1', '2', 'fizz']
    >>> fizzbuzz(16)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', \
'fizz', '13', '14', 'fizz buzz', '16']

    """

    basic_list = [str(x) for x in range(1, n + 1)]
    for item in range(1, n + 1):
        if item % 15 == 0:
            basic_list[item - 1] = 'fizz buzz'
        elif item % 5 == 0:
            basic_list[item - 1] = 'buzz'
        elif item % 3 == 0:
            basic_list[item - 1] = 'fizz'
    return basic_list
