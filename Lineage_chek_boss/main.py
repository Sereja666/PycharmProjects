import configparser
import datetime
import os
import time
from pathlib import Path
import pyautogui
import pytesseract
import requests


# Конфиг
config = configparser.ConfigParser()
config.read(Path(os.getcwd(), 'config.ini'), encoding="utf8")
bot_token = config['TG_bot']['BOT_TOKEN']
bot_chatID = config['TG_bot']['bot_chatID']
time_sleep = int(config['time_sleep']['time_sleep'])
x = int(config['coordinates_chat']['x'])
y = int(config['coordinates_chat']['y'])
height = int(config['coordinates_chat']['height'])
width = int(config['coordinates_chat']['width'])
tesseract_OCR = config['tesseract_OCR']['tessdata-dir']
tesseract_exe = config['tesseract_OCR']['exe']
screen = bool(config['screen']['screen'])
print(type(screen), screen)

pytesseract.pytesseract.tesseract_cmd = tesseract_exe


def tg(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


old_mess = None

dict_data = {'Королева Муравьев': "",

             'закен': "",
             'орфен': "",
             'ядро': "",
             'баюм': "",}

try:
    while True:

        # Получаем текст из чата
        chat_text = pyautogui.screenshot(region=(x, y, width, height))

        # Преобразуем изображение в текст
        chat_text = chat_text.convert('L')  # Преобразование изображения в оттенки серого
        threshold = 120  # Пороговое значение для бинаризации
        chat_text = chat_text.point(lambda p: p > threshold and 255)  # Бинаризация изображения
        if screen:
            chat_text.save('screen.png')
        tessdata_dir_config = fr'--tessdata-dir "{tesseract_OCR}"'
        chat_message = pytesseract.image_to_string(chat_text, lang='rus+eng', config=tessdata_dir_config)
        if screen:
            print(repr(chat_message))
        if "возродился Рейдовый" in chat_message:
            list_mess = chat_message.split('\n')
            for line in list_mess:
                if "возродился рейдовый" in line.lower():
                    boss_name = line.lower().replace('возродился рейдовый босс', '').replace('.', '').strip()
                    if boss_name in dict_data:
                        current_time = datetime.datetime.now()
                        if current_time > dict_data[boss_name] + datetime.timedelta(minutes=20):

                            # tg(f'{current_time.strftime('%d.%m.%Y %H:%M')} - {line}')
                            print(f'{current_time.strftime('%d.%m.%Y %H:%M')} - {line}')
                            time.sleep(5)
                            old_mess = line
                            dict_data[boss_name] = current_time
                            print(dict_data)
                            print('='*10)
                            break
                    else:
                        print(f'неизвестный босс {boss_name}')


        # Делаем паузу перед следующей проверкой
        time.sleep(time_sleep)
except Exception as err:
    print(err)
    time.sleep(30)