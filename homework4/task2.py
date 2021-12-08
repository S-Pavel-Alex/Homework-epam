from unittest.mock import Mock


def count_dots_on_i(url: str) -> int:
    """Count i item"""
    try:
        text = connect_url_mock(url)
        total = text.count('i')
    except Exception:
        raise ValueError(f"Unreachable {url}")
    return total


def connect_url_mock(url: str):
    """Create connect and read text"""
    mock_object = Mock()
    mock_object.url = url
    mock_object.text = 'i say i'
    return mock_object.text
