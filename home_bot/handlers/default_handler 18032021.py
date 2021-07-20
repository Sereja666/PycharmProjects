import subprocess

import transliterate
from aiogram import types
import re
import datetime

# Если запускаете код отдельно от этого репозитория, то закомментируйте следующую строку:
from aiogrambot.misc import dp

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# ... и замените её на:
# from misc import dp


@dp.message_handler(content_types=types.ContentTypes.ANY, state="*")
async def all_other_messages(message: types.Message):
    ot_polzaka = message.text
    ot_polzaka = ot_polzaka.lower()  # привожу всё к мелким буквам
    if re.search(r'\bкек\b', ot_polzaka):
        await message.answer("чебурек")
    elif re.search(r'\bсписок команд\b', ot_polzaka):  # СПисок команд
        await message.answer("""
        Писать можно маленькими и большими буквами
        1. Список команд
        ++++++++++++++++++++++++++++++++++++++++++
        2. предлагаю ...
        3. Что в списке
        4. Отчисти/сотри/удали список 
        ++++++++++++++++++++++++++++++++++++++++++

        Быстрые ответы:
            5. УК Еврейский дом
            6. какой номер аварийки ?         
            7. какой номер бухгалтерии ?
            8. какой номер юристов ?


        ++++++++++++++++++++++++++++++

        """)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    elif re.search(r'\bпредлагаю\b', ot_polzaka):  # СПисок команд
        res = []
        res.append(message.text)
        text = res[0]
        ogrizok = (text[text.find('предлагаю') + 9:])
        f = open('1.txt', 'a')
        f.write(ogrizok + "\n")
        f.close()
        await message.answer("записал: " + ogrizok)
        # await message.reply("Этот бот принимает только текстовые сообщения!")
    elif re.search(r'\bчто\b', ot_polzaka) and re.search(r'\bв\b', ot_polzaka) and re.search(r'\bсписке\b', ot_polzaka):
        f = open('1.txt', 'r')
        await message.answer("в списке предложений:  ")
        await message.answer(f.read())
        f.close()
    elif re.search(r'\bотчисти список\b', ot_polzaka) or re.search(r'\bсотри список\b', ot_polzaka) or re.search(
            r'\bудали список\b', ot_polzaka):
        open('1.txt', 'w').close()
        await message.answer("список предложений теперь пуст")

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    elif re.search(r'\bкто дежурит\b', ot_polzaka):
        now = datetime.datetime.now()
        f = open('\\\\hranilka\\AVAGroup\\AVA\\ИТ\\!Общие документы\\графики дежурств\\ДежурствоБота.txt', 'r')
        await message.answer(
            "сегодня " + now.strftime("%d-%m-%Y") + " от рождества Христова. \n " + "     Дежурства:  \n" + f.read())

        f.close()


    elif re.search(r'\bук еврейский\b', ot_polzaka):
        await message.answer(" гавно!  ")
    # Аварийка
    elif re.search(r'\bкакой \b', ot_polzaka) and re.search(r'\bномер\b', ot_polzaka) and re.search(r'\bаварийки\b',
                                                                                                    ot_polzaka):
        await message.answer("+79384061610")

    elif re.search(r'\bнас\b', ot_polzaka) and re.search(r'\bтопят\b', ot_polzaka):
        await message.answer("номер аварийки +79384061610")

    elif re.search(r'\bнас\b', ot_polzaka) and re.search(r'\bзатопили\b', ot_polzaka):
        await message.answer("номер аварийки +79384061610")
    elif re.search(r'\bменя\b', ot_polzaka) and re.search(r'\bтопят\b', ot_polzaka):
        await message.answer("номер аварийки +79384061610")
    elif re.search(r'\bменя\b', ot_polzaka) and re.search(r'\bзатопили\b', ot_polzaka):
        await message.answer("номер аварийки +79384061610")
    # -----------------------------------------------------------------------------
    elif re.search(r'\bкакой\b', ot_polzaka) and re.search(r'\bномер\b', ot_polzaka) and re.search(r'\bбухгалтерии\b',
                                                                                                   ot_polzaka):
        await message.answer("+79604738776")

    elif re.search(r'\bкакой\b', ot_polzaka) and re.search(r'\bномер\b', ot_polzaka) and re.search(r'\bюристов\b',
                                                                                                   ot_polzaka):
        await message.answer("+79649128753")