import queue
from itertools import chain
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    stack = queue.LifoQueue()
    stack.put(tree)
    total = 0
    while not stack.empty():
        data = stack.get()
        if isinstance(data, (int, str, bool)):
            if data == element:
                total += 1
        elif isinstance(data, (list, tuple, set)):
            for i in data:
                stack.put(i)
        elif isinstance(data, dict):
            for item in chain(data.keys(), data.values()):
                stack.put(item)
    return total
