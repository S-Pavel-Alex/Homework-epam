from typing import Any
from collections import abc
from itertools import chain


def find_occurrences(tree: dict, element: Any) -> int:
    if isinstance(tree, int) or isinstance(tree, str)\
            or isinstance(tree, bool):
        if tree == element:
            return 1
        else:
            return 0
    if isinstance(tree, abc.Sequence):
        return sum(find_occurrences(t, element) for t in tree)
    if isinstance(tree, abc.Mapping):
        return sum(find_occurrences(t, element)
                   for t in chain(tree.keys(), tree.values()))


