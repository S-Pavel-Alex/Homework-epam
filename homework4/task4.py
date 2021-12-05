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
    for item in basic_list:
        if int(item) % 3 == 0 and int(item) % 5 == 0:
            item_index = basic_list.index(item)
            basic_list[item_index] = 'fizz buzz'
        elif int(item) % 5 == 0:
            item_index = basic_list.index(item)
            basic_list[item_index] = 'buzz'
        elif int(item) % 3 == 0:
            item_index = basic_list.index(item)
            basic_list[item_index] = 'fizz'
    return basic_list
