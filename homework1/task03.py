"""
Write down the function, which reads input line-by-line, and find maximum and
 minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        value_min = int(fi.readline())
        value_max = value_min
        for line in fi:
            try:
                line = int(line.strip())
                if value_min >= line:
                    value_min = line
                elif value_max <= line:
                    value_max = line
            except ValueError:
                pass
    return value_min, value_max
