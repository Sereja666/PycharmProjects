import requests
from bs4 import BeautifulSoup
import re
from delivery.misc import product_code

def where_product():
    url = f'https://gdeposylka.ru/courier/eshun/tracking/{product_code}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all('span', class_='td info status-iconed')

    where = []
    for quote in quotes:
        a = quote.text
        a = re.sub(" +", " ", a)
        a = a.replace('\n', ' ')
        where.append(a)
    where.reverse()

    where_txt = ''
    for n in where:
        where_txt += n + '\n'

    f = open("old.txt", "r")
    text = f.read()
    f.close()

    if text != where_txt:

        f = open("old.txt", "w")
        f.write(where_txt)
        f.close()

        return where
    else:
        return False
