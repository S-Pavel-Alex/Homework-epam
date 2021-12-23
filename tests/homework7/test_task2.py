from homework7.task2 import backspace_compare


def test_backspace_compare_correct():
    assert backspace_compare("ab#c", "ad#c") is True
    assert backspace_compare("a##c", "#a#c") is True
    assert backspace_compare(" ## ", "# # ") is True


def test_backspace_compare_incorrect():
    assert backspace_compare("a#c", "b") is False
    assert backspace_compare("A#C", "a#c") is False
