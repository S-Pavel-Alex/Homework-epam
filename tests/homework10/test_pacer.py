import unittest.mock

from homework10.percer_multi import dollar_covert, base_pages, scraping_href

HTML_DOLLAR = ('<Valute ID="R01235">'
               '<NumCode>840</NumCode>'
               '<CharCode>USD</CharCode>'
               '<Nominal>1</Nominal>'
               '<Name>Доллар США</Name>'
               '<Value>75,7668</Value>'
               '</Valute>')

HTML_BASE_PAGES = ('<a> class=tab__subnav__item"A"</a>'
                   '<a> class=tab__subnav__item"B"</a>'
                   '<a> class=tab__subnav__item"B"</a>'
                   '<a> class=tab__subnav__item"B"</a>')


HTML_SCRAP = '<td class=table__td table__td--big><a href="/b"</a></td>'


def test_dollar_covert():
    with unittest.mock.patch('requests.get') as mock_obj:
        mock_obj().text = HTML_DOLLAR
        assert dollar_covert() == 75.7668


def test_base_pages():
    with unittest.mock.patch('requests.get') as mock_obj:
        mock_obj().text = HTML_BASE_PAGES
        lst = []
        for i in base_pages():
            lst.append(i)
        assert lst == []


def test_scraping_href():
    with unittest.mock.patch('requests.get') as mock_obj:
        mock_obj().text = HTML_SCRAP
        assert scraping_href('example.ru') == ['https://markets.busines'
                                               'sinsider.com/b']
