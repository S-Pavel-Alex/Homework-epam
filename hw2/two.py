from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """Given an array of size n, find the most common and the least common
     elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other."""
    my_dict = {}
    final_dict = {}
    for element in inp:
        if element in my_dict:
            my_dict[element] += 1
        else:
            my_dict[element] = 1
    for k, v in my_dict.items():
        final_dict[v] = k
    key_max = max(final_dict)
    key_min = min(final_dict)
    count = inp.count(final_dict[key_max])
    if count >= len(inp)//2:
        return final_dict[key_max], final_dict[key_min]
