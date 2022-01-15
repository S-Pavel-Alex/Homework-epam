import json
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor

import requests
from bs4 import BeautifulSoup as BS


def dollar_covert():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    req = requests.get(url)
    soup = BS(req.text, 'lxml')
    value = soup.find('valute', id="R01235").find('value')
    return float(value.text.replace(',', '.'))


def base_pages():
    url = 'https://markets.businessinsider.com/index/components/s&p_500'
    res = requests.get(url)
    soup = BS(res.text, 'lxml')
    pages = soup.find_all('a', {'class': 'tab__subnav__item'})
    for page in pages[1:]:
        yield '{}/{}'.format(url, page.text.strip())


def scraping_href(page):
    """Function scraping link companies"""
    all_href = []
    req = requests.get(page)
    r = req.text
    soup = BS(r, "lxml")
    all_companies = soup.find_all(class_='table__td table__td--big')
    for company in all_companies:
        all_href.append('https://markets.businessinsider.com' +
                        company.find('a').get('href'))
    return all_href


def give_html(url):
    req = requests.get(url)
    return req.text


def data_companies(lst):
    all_companies_data = []
    with ThreadPoolExecutor() as executor:
        html_all = executor.map(give_html, lst)
    for html in html_all:
        soup = BS(html, 'lxml')
        name = soup.find(class_="price-section__label").text.strip()
        price = soup.find('span',
                          {'class': 'price-section__current-value'}
                          ).text.replace(',', '')
        price = round(float(price) * dollar_covert(), 2)
        code = soup.find(
            class_="price-section__category"
        ).find('span').text.split()[1]
        p_e = soup.find(class_="snapshot__header", text='P/E Ratio')
        p_e = float(p_e.find_parent().text.split()[0].replace(',', '')
                    if p_e else 'inf')
        wick_low = soup.find(class_="snapshot__header", text='52 Week Low')
        wick_low = float(
            wick_low.find_parent().text.split()[0].replace(',', '') if wick_low
            else '-inf')
        wick_high = soup.find(class_="snapshot__header", text='52 Week High')
        wick_high = float(
            wick_high.find_parent().text.split()[0].replace(',', '')
            if wick_high else '-inf')
        win_percent = ((wick_high - wick_low) / wick_low) * 100
        win_percent = float(format(win_percent, '.0f'))
        all_companies_data.append({
            'code': code,
            'name': name,
            'price': price,
            'P/E': p_e,
            'potential profit': win_percent
        })
    return all_companies_data


def top_ten(companies, item, reverse):
    return sorted(companies, key=lambda company: company[item],
                  reverse=reverse)[:10]


def record(top, name_top):
    with open(f'data_json/{name_top}.json', 'w') as file:
        json.dump(top, file, indent=4)


def main():
    href_list = list()
    with ThreadPoolExecutor() as executor:
        href_all = executor.map(scraping_href, base_pages())
    for href in href_all:
        href_list.extend(href)

    def gen_list_list(lst, n):
        for val in range(0, len(lst), n):
            yield lst[val:val+n]

    list_list = []

    for i in gen_list_list(href_list, len(href_list)//4):
        list_list.append(i)

    all_data_companies = []
    with ProcessPoolExecutor(4) as executor:
        companies = executor.map(data_companies, list_list)

    for company in companies:
        all_data_companies.extend(company)

    growth_list = []
    for page in base_pages():
        req = requests.get(page)
        html = req.text
        soup = BS(html, "lxml")
        companies_data = soup.find(class_='table__tbody').find_all(
            'tr')
        for item in companies_data:
            column = item.find_all('td')
            growth = column[7].text.split()[1]
            growth = float(growth.replace('%', ''))
            growth_list.append(growth)
    for i in range(len(growth_list)):
        all_data_companies[i]['growth'] = growth_list[i]

    js_param = namedtuple('js_param', ['file', 'attribute', 'reverse'])
    top_list = [
        js_param('top_ten_price', 'price', True),
        js_param('top_ten_p_e', 'P/E', False),
        js_param('top_ten_growth', 'growth', True),
        js_param('top_ten_profit', 'potential profit', True)
    ]
    for param in top_list:
        js_object = top_ten(all_data_companies, param.attribute, param.reverse)
        record(js_object, param.file)


if __name__ == '__main__':
    main()
