import requests
import lxml
from bs4 import BeautifulSoup
import schedule
import time
from colorama import Fore


def job():
    url = 'https://europaplus.ru/brigadau'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    stars = soup.find_all('p',
                          class_='typography typography_mark_medium typography_type_text typography_size_max typography_color_black horoscope-card__name')
    goroskop_dict = soup.find_all('p',
                                  class_='typography typography_type_text typography_size_middle typography_color_black horoscope-card__forecast')
    stroka = ''

    peopledict = ['Раки', "Водолеи", "Рыбы", "Стрельцы"]
    for i in range(len(goroskop_dict)):
        # for people in peopledict:
        if "Рак" in goroskop_dict[i].text:
            stroka = Fore.RED + (goroskop_dict[i].text)
        elif "Рыбы" in goroskop_dict[i].text:
            stroka = Fore.RED + (goroskop_dict[i].text)

        elif "Стрельцы" in goroskop_dict[i].text:
            stroka = Fore.RED + (goroskop_dict[i].text)
        elif "Водолеи" in goroskop_dict[i].text:
            stroka = Fore.BLUE + (goroskop_dict[i].text)
        else:
            stroka = Fore.GREEN + (goroskop_dict[i].text)
        print(stroka)

job()