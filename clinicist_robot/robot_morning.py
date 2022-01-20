# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import pyautogui
import pyperclip
import win32api
import ctypes

from config import login_site, password_site




def get_layout():  # смена языка
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    if hex(pf(0)) == '0x4190419':
        pyautogui.hotkey('alt', 'shiftleft')


def site():
    # try:
        # авторизация
        driver =  webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://voicebox.mtt.ru/campaigns/makeCampaign")
        el1 = driver.find_element_by_name('login')
        el1.send_keys(login_site)
        time.sleep(1)
        el1 = driver.find_element_by_name('password')
        el1.send_keys(password_site)
        time.sleep(1)
        el1 = driver.find_element_by_xpath('/html/body/section/div/section/div/div/section/form/div[2]/div/button')
        el1.click()
        print('1. авторизовался')

        # от
        el2 = driver.find_element_by_xpath('/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[2]/div[2]/div[1]/ul[3]/li[2]/span[1]/input')
        el2.clear()
        el2.send_keys('10:00')
        time.sleep(1)
        print('2. От')

        # до
        el2 = driver.find_element_by_xpath("/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[2]/div[2]/div[1]/ul[3]/li[2]/span[2]/input")
        el2.clear()
        el2.send_keys('20:00')
        time.sleep(1)
        print('3. до')

        # Количество звонков
        el3 = driver.find_element_by_xpath('/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[2]/div[2]/div[2]/ul[1]/li[2]/div/div/div/div[1]/input')
        el3.click()
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("ENTER")
        print('4. Количество звонков')

        # Интервал между попытками
        el4 = driver.find_element_by_xpath(
            '/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[2]/div[2]/div[2]/ul[2]/li[2]/div/div/div/div[1]/input')
        el4.click()
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("ENTER")
        print('5. Интервал между попытками')

        # Максимум линий
        el5 = driver.find_element_by_xpath('/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[2]/div[2]/div[2]/ul[3]/li[2]/div/div/div/div[1]/input')
        el5.click()
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("down")
        pyautogui.press("ENTER")
        print('6. Максимум линий')

        # Выбор сценария
        el6 = driver.find_element_by_xpath(
            '/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[3]/ul/li[1]/div[2]/div/div/div/div[1]/input')
        el6.clear()
        el6.send_keys('уведомление о приеме')
        pyautogui.press("ENTER")
        print('7. Выбор сценария')

        # Выбор номера
        el7 = driver.find_element_by_xpath(
            '/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[3]/ul/li[2]/div[2]/div/div/div/div[1]/input')
        el7.clear()
        el7.send_keys('78612055437')
        pyautogui.press("ENTER")

        # Загрузить файл
        el8 = driver.find_element_by_xpath('/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[4]/div[2]/ul[2]/li[2]/div')
        el8.click()




        get_layout() #смена языка
        exl_input = r'C:\Users\Sereja\Documents\Vova\MyData.csv'
        time.sleep(2)
        pyperclip.copy(exl_input)
        time.sleep(2)
        # clipboard_content = pyperclip.paste()
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press("ENTER")
        time.sleep(1)
        print('8.Загрузить файл')


        # чекбокс согласия
        el9 = driver.find_element_by_xpath('/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[4]/div[2]/ul[2]/li[3]/div/label')
        el9.click()
        print('9. чекбокс согласия')

        # кнопка сохранить
        el10 = driver.find_element_by_xpath('/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[6]/div[2]/button')
        el10.click()
        time.sleep(1)
        print('10. кнопка сохранить')

        try:
            # кнопка Да, запустить
            el11 = driver.find_element_by_xpath(
                "/html/body/section/div/section[2]/div/div/section/section/div[2]/div/div[1]/div[2]/div[3]/button[1]")
            el11.click()
            print('11. кнопка Да, запустить')
        except Exception:
            print('кнопка Да, запустить не появилась')

        time.sleep(10)


        # закрыть чтоб не засорять процессы винды

        driver.quit()
    # except Exception:
    #     print('что то сломалось, запускаюсь заново')
    #     site()

site()