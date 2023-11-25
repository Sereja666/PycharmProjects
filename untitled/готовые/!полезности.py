# Чтение данных, вводимых с клавиатуры
import pyinstaller as pyinstaller

name = input('Enter your name:')
print(name)
# или так же
print('What is your name?')
name = input()
print(name)

# _________________________путь где работать_______________________
os.chdir("I:\\Обмен\\ИТ\\Заявки на оплату\\2019-01-03\\Краснодар\\1") # выбираю путь где работать


# Открыть файлик
import os
os.startfile(r'C:\\Users\\ass\\AppData\\Local\\Programs\\Opera GX\\launcher.exe')

# Создать папку
import os
os.makedirs(r"C:\tmp\кек\first\second\third")

# _______________________________________________________________
# эмитация нажатия
import pyautogui
# эмитация нажатия ПАУЗА
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.press('4')

#__________узнать имя компа
import socket
print(socket.gethostname())

#_______транслит с русского
from transliterate import translit, get_available_language_codes

print(translit(u"Лорем ипсум долор сит амет", reversed=True))

#___________________________превратить в exe
pip install pyinstaller
cd C:\Py
pyinstaller -F 1.py
#Здесь нас интересует папка dist, остальное можно удалить. В папке у нас появилось приложение av_zp.exe. Давайте запустим его


#_____________есть ли файл ________________
import os

if os.path.exists("C:\\Program Files (x86)\\1cv8\\8.3.15.1830\\bin1"):
     print ("Файл найден")
else:
     print ("Файл не найден")