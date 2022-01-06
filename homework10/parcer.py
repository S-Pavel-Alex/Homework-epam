import requests

from bs4 import BeautifulSoup as BS

url = 'https://markets.businessinsider.com/index/components/s&p_500?p=1'

r = requests.get(url)
html = BS(r.content, "html.parser")


for el in html.select(".table__tbody"):
    e = el.find_all('a', title)
    print(e)