from concurrent.futures.process import ProcessPoolExecutor
from typing import Tuple
from bs4 import BeautifulSoup as BS
import requests
from concurrent.futures import ThreadPoolExecutor

def dollar_covert():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    req = requests.get(url)
    soup = BS(req.text, 'lxml')
    value = soup.find('valute', id="R01235").find('value')
    return float(value.text.replace(',', '.'))

data = [i for i in range(1, 12)]
def scraping_href(page):
    """Function scraping link companies"""

    url = 'https://markets.businessinsider.com/index/components/s&p_500?p='
    req = requests.get(url + str(page))
    r = req.text
    soup = BS(r, "lxml")
    all_companies = soup.find_all(class_='table__td table__td--big')
    return all_companies

def give_html(url):
    req = requests.get(url)
    return req

def data_companies(l):
    for url in l:
        req = requests.get(url)
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
        for page in data:  
            req = requests.get('https://markets.businessinsider.com/index/components/s&p_500?p=' + str(page))
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


def main():
    all_href  = list()
    with ThreadPoolExecutor() as execute:
        href = tuple(execute.map(scraping_href, data))
    for h in href:
        for q in h:
            all_href.append('https://markets.businessinsider.com' + q.find('a').get('href'))

    # with ThreadPoolExecutor() as execute:
    #     html = tuple(execute.map(give_html, all_href))
  # Поробывать написать цикл лист в листе  
    l1 = all_href[:124]
    l2 = all_href[125:249]
    l3 = all_href[250:374]
    l4 = all_href[375:496]
    l_all =[]
    l_all.append(l1)
    l_all.append(l2)
    l_all.append(l3)
    l_all.append(l4)

    with ProcessPoolExecutor(4) as execute:
        companies = [*map(data_companies, l_all)]

    for c in companies:
        print(c)

main()