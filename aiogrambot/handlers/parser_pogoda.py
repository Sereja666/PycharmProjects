import re
import requests
import lxml
from bs4 import BeautifulSoup


def weather():
    url = 'https://pogoda.mail.ru/prognoz/krasnodar/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    temperature = soup.find_all('div', class_='information__content__period__temperature')

    pogoda = soup.find_all('div', class_='information__content__additional__item')

    day = ("Погода днём " + temperature[0].text)
    evening = ("Погода вечером " + temperature[1].text)
    feeling = (pogoda[0].text).strip(' \t\n\r')
    cloud = (pogoda[1].text).strip(' \t\n\r')
    veter = (re.sub('[\s+]', ' ', pogoda[4].text) )
    veter1 = veter.strip(' \t\n\r')
    # print(day)
    # print(evening)
    # print(feeling)
    # print(cloud)
    # print (veter.strip(' \t\n\r'))

    stroka = (day + "\n" + evening + "\n" + feeling + "\n" + cloud + "\n" + veter1)
    return stroka