import requests
import requests_mock


def connect_function():
    session = requests.Session()
    adapter = requests_mock.Adapter()
    session.mount('mock://', adapter)
    adapter.register_uri('GET', 'mock://test.com')
    resp = session.get('mock://test.com')
    return connect_function()


