from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


def unpacking(file_name) -> Iterator:
    """Unpacking files

    Args:
        file_name (str): file with data

    Yields:
        Iterator: iterator 
    """
    with open(file_name) as file:
        yield from (int(item) for item in file)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    iterators = (unpacking(file) for file in file_list)
    return iter(merge(*iterators))
    