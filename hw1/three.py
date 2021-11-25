from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Write down the function, which reads input line-by-line, and find
    maximum and minimum values. Function should return a tuple with the max
     and min values."""
    with open(file_name) as fi:
        value_min = int(fi.readline())
        value_max = value_min
        for line in fi:
            try:
                line_convert_int = int(line.strip())
                if value_min > line_convert_int:
                    value_min = line_convert_int
                elif value_max < line_convert_int:
                    value_max = line_convert_int
            except ValueError:
                pass
    return value_min, value_max
