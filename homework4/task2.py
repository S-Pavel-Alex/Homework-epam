from unittest.mock import Mock


def count_dots_on_i(url: str) -> int:
    """Count i item"""
    if connect_url_mock(url).status_code != 200:
        raise ValueError(f"Unreachable {url}")
    text = connect_url_mock(url).text
    total = text.count('i')
    return total


def connect_url_mock(url: str):
    """Create connect and read text"""
    mock_object = Mock()
    mock_object.url = url
    mock_object.text = 'i say i'
    mock_object.status_code = 200
    return mock_object
