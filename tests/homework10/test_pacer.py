import unittest.mock
from bs4 import BeautifulSoup

from homework10.percer_multi import dollar_covert, base_pages, scraping_href, \
    give_html, data_companies

HTML_DOLLAR = ('<Valute ID="R01235">'
               '<NumCode>840</NumCode>'
               '<CharCode>USD</CharCode>'
               '<Nominal>1</Nominal>'
               '<Name>Доллар США</Name>'
               '<Value>75,7668</Value>'
               '</Valute>')

HTML_BASE_PAGES = (
    '<a href="/index/components/s&amp;'
    'p_500/A" class="tab__subnav__item ">A</a>'
    '<a href="/index/components/s&amp;'
    'p_500/B" class="tab__subnav__item ">B</a>'
    '<a href="/index/components/s&amp;'
    'p_500/C" class="tab__subnav__item ">C</a>')


HTML_SCRAP = '<td ' \
             'class="table__td table__td--big">' \
             '<a href="/stocks/aos-stock"' \
             ' title="A.O. Smith Corp.">A.O. Smith Corp.</a>' \
             '</td>'


HTML_FOR_TEST_SCRAPING = \
    '<span class="price-section__label">A.O. Smith Corp. </span>'\
    '<span class="price-section__current-value">80.59</span>'\
    '<span class="price-section__category">Stock <span>, AOS</span></span>'\
    '<div class="snapshot__data-item">'\
    '25.06<div class="snapshot__header">P/E Ratio</div></div>'\
    '<div class="snapshot__data-item snapshot__data-item--small">'\
    '52.08<div class="snapshot__header">52 Week Low</div></div>'\
    '<div class="snapshot__data-item snapshot__'\
    'data-item--small snapshot__data-item--right">'\
    '86.74<div class="snapshot__header">52 Week High</div></div>'


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
        assert lst == [
            'https://markets.businessinsider.com/index/components/s&p_500/B',
            'https://markets.businessinsider.com/index/components/s&p_500/C'
        ]


def test_scraping_href():
    with unittest.mock.patch('requests.get') as mock_obj:
        mock_obj().text = HTML_SCRAP
        assert scraping_href('example.ru') == ['https://markets.busines'
                                               'sinsider.com/stocks/aos-stock']


def test_give_html():
    with unittest.mock.patch('requests.get') as mock_obj:
        mock_obj().text = 'Hi'
        assert give_html('example.com') == 'Hi'


# def test_data_companies():
#     with unittest.mock.patch('concurrent.futures.ThreadPoolExecutor') as mock_obj:
#         mock_obj().map = [HTML_FOR_TEST_SCRAPING, ]
#         assert data_companies(['http://example.c']) == []


def test():
    soup = BeautifulSoup(HTML_FOR_TEST_SCRAPING, 'lxml')
    assert soup.find(class_="price-section__label").text.strip() == 'A.O. Smith Corp.'