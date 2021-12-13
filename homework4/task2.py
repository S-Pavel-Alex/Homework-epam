import requests


def count_dots_on_i(url: str) -> int:
    """Count i item."""
    try:
        text = requests.get(url).text
    except Exception:
        raise ValueError("Unreachable {url}")
    i_count = text.count('i')
    return i_count
