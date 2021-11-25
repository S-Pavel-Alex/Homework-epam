import doctest
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

    basic_list = [x for x in range(1, n + 1)]
    fiz_buz_list = []
    for item in basic_list:
        if item % 3 == 0 and item % 5 == 0:
            fiz_buz_list.append('fizz buzz')
        elif item % 5 == 0:
            fiz_buz_list.append('buzz')
        elif item % 3 == 0:
            fiz_buz_list.append('fizz')
        else:
            fiz_buz_list.append(str(item))
    return fiz_buz_list


if __name__ == "__main__":
    doctest.testmod()
