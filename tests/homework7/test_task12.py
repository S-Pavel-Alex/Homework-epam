import pytest

from homework7.task12 import find_occurrences


example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": [True, "list", 4, "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": 0,
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": 0}],
        }
     },
    "fourth": "RED",
}


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((example_tree, "RED"), 5),
        ((example_tree, 'of'), 1),
        ((example_tree, "nested_key"), 1),
        ((example_tree, "jhl"), 1),
        ((example_tree, 0), 2),
        ((example_tree, 4), 1),
        ((example_tree, 'example'), 0),
        ((example_tree, ''), 0),
        ((example_tree, True), 1),
        ((example_tree, 'fourth'), 1),
        ((example_tree, 'f'), 0)
    ],
)
def test_find_occurrences(test_input, expected):
    assert find_occurrences(*test_input) == expected
