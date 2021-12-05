import urllib.request


def count_dots_on_i(url: str) -> int:
    """Count i item"""
    text = connect_url(url)
    total = text.count('i')
    return total


def connect_url(url: str):
    """Create connect and read text"""
    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')
