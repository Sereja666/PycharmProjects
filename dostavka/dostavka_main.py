import requests
from bs4 import BeautifulSoup
import re


def gde_tovar():
    url = 'https://gdeposylka.ru/courier/eshun/tracking/ZESZE2024463187YQ'
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
    print(where_txt)
    text = ''

    # with open("old.txt", "r") as f:
    #     text = f.read()

    f = open("old.txt", "r")
    text = f.read()
    f.close()

    if text != where_txt:

        f = open("old.txt", "w")
        f.write(where_txt)
        f.close()
        print(f' return {where}')
        return where
    else:
        print(' return False')
        return False
