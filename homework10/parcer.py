import requests

from bs4 import BeautifulSoup as BS

url = 'https://markets.businessinsider.com/index/components/s&p_500?p=1'

r = requests.get(url)
html = BS(r.content, "html.parser")


for el in html.select('tbody > tr'):
    title = el.select('td > a')
    print(title[0].text)
