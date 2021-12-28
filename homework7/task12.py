from itertools import chain
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    stack = list()
    stack.append(tree)
    total = 0
    while stack:
        data = stack.pop()
        if isinstance(data, (int, str, bool)):
            if data == element:
                total += 1
        elif isinstance(data, (list, tuple, set)):
            for i in data:
                if isinstance(i, (list, tuple, set, dict)):
                    stack.append(i)
                else:
                    if i == element:
                        total += 1
        elif isinstance(data, dict):
            for item in chain(data.keys(), data.values()):
                if isinstance(item, (list, tuple, set, dict)):
                    stack.append(item)
                else:
                    if item == element:
                        total += 1
    return total
