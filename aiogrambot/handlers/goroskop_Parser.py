import subprocess

import schedule
import transliterate
from aiogram import types
import re
import datetime
import asyncio
from contextlib import suppress
import schedule
import time
# Если запускаете код отдельно от этого репозитория, то закомментируйте следующую строку:
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

from aiogrambot.misc import dp, bot

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, message

# ... и замените её на:
# from misc import dp



import requests
import lxml
from bs4 import BeautifulSoup

def goroskop():
    url = 'https://europaplus.ru/brigadau'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    stars = soup.find_all('p', class_='typography typography_mark_medium typography_type_text typography_size_max typography_color_black horoscope-card__name')
    goroskop_dict = soup.find_all('p', class_='typography typography_type_text typography_size_middle typography_color_black horoscope-card__forecast')


    stroka = ''
    simvol = {"Овен": '♈', "Телец": '♉', "Близнецы": '♊', "Рак": '♋', "Лев": '♌', "Дева": '♍', "Весы": '♎', "Скорпион": '♏', "Стрелец": '♐', "Козерог": '♑',
              "Водолей": '♒', "Рыбы": '♓'}
    for i in range(len(goroskop_dict)):
            stars1 = (simvol[stars[i].text])
            goroskop1 = (goroskop_dict[i].text)
            stroka += (stars1 + " " + goroskop1 + '\n\n')


    return stroka




