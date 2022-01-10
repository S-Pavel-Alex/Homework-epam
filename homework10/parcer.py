from typing import Generator
import requests
import json
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

from bs4 import BeautifulSoup as BS




def dollar_covert():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    req = requests.get(url)
    soup = BS(req.text, 'lxml')
    value = soup.find('valute', id="R01235").find('value')
    return float(value.text.replace(',', '.'))


def pages_table() -> Generator:
    """Fuction return html code from each pages"""
    url = 'https://markets.businessinsider.com/index/components/s&p_500?p='
    for page in range(1, 12):
        url_all = url + str(page)
        yield url_all


def scraping_href():
    """Function scraping link companies"""
    for html in pages_table():
        req = requests.get(html)
        r = req.text
        soup = BS(r, "lxml")
        all_companies = soup.find_all(class_='table__td table__td--big')
        for company in all_companies:
            # company_title = company.find('a').text
            company_href = 'https://markets.businessinsider.com' + company.find('a').get('href')
            yield company_href



def data_companies(href):
    req = requests.get(href)
    html = req.text
    soup = BS(html, 'lxml')
    name = soup.find(class_="price-section__label").text.strip()
    price = soup.find('span', {'class': 'price-section__current-value'}).text.replace(',', '')
    price = round(float(price) * dollar_covert(), 2)
    code = soup.find(class_="price-section__category").find('span').text.split()[1]
    p_e = soup.find(class_="snapshot__header", text='P/E Ratio')
    p_e = float(p_e.find_parent().text.split()[0].replace(',', '') if p_e else 'inf')
    wick_low = soup.find(class_="snapshot__header", text='52 Week Low')
    wick_low = float(wick_low.find_parent().text.split()[0].replace(',', '') if wick_low else '-inf')
    wick_high = soup.find(class_="snapshot__header", text='52 Week High')
    wick_high = float(wick_high.find_parent().text.split()[0].replace(',', '') if wick_high else '-inf')
    win_procent = ((wick_high - wick_low) / wick_low) * 100
    win_procent = float(format(win_procent, '.0f'))
    for page in pages_table():
        req = requests.get(page)
        html = req.text
        soup = BS(html, "lxml")
        companies_data = soup.find(class_='table__tbody').find_all('tr')
        for item in companies_data:
            column = item.find_all('td')
            win_lose_year =column[7].text.split()[1]
            win_lose_year = float(win_lose_year.replace('%', ''))  
    return {
        'code': code,
        'name': name, 
        'price': price, 
        'P/E': p_e, 
        'growth': win_lose_year,
        'potential profit': win_procent
            }

def top_ten(companies, item, reverse):
    return sorted(companies, key=lambda company: company[item], reverse=reverse)[:10]


def record(top, name_top):
    with open(f'{name_top}.json', 'w') as file:
        json.dump(top, file, indent=4)


def main():
    with ProcessPoolExecutor(4) as executor:       
        companies = tuple(executor.map(data_companies, scraping_href()))

    top_ten_price = top_ten(companies, 'price', True)
    top_ten_p_e = top_ten(companies, 'P/E', False)
    top_ten_growth = top_ten(companies, 'growth', True)
    top_ten_potentional_profit = top_ten(companies, 'potential profit', True)
 
    record(top_ten_price, 'top_ten_price')
    record(top_ten_p_e, 'top_ten_p_e')
    record(top_ten_growth, 'top_ten_growth')
    record(top_ten_potentional_profit, 'top_ten_potentional_profit')

if __name__ == '__main__':
    main()

