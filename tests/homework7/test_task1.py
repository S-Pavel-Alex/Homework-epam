from homework7.task1 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": [True, "list", 4, "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": 4}],
        }
     },
    "fourth": "RED",
}


def test_find_occurrences():
    assert find_occurrences(example_tree, "RED") == 5
    assert find_occurrences(example_tree, 4) == 2
    assert find_occurrences(example_tree, 'example') == 0
    assert find_occurrences(example_tree, '') == 0
    assert find_occurrences(example_tree, True) == 1
    assert find_occurrences(example_tree, 'fourth') == 1
    assert find_occurrences(example_tree, 'f') == 0
