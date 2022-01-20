# -*- coding: utf-8 -*-
import os
import shutil

from selenium import webdriver
import time
import pyautogui
import pyperclip
import win32api
import ctypes

from config import login_site, password_site, new_place, path


def search_file():

    for root, dirs, files in os.walk(path):
        for file in files:
            if  'Отчет_по_кампании_Новая_кампания' in file:
                path_file = os.path.join(root,file)
                return path_file

def site_evning():
    # try:
    # авторизация
    driver =  webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://voicebox.mtt.ru/campaigns/myCampaigns")
    el1 = driver.find_element_by_name('login')
    el1.send_keys(login_site)
    time.sleep(1)
    el1 = driver.find_element_by_name('password')
    el1.send_keys(password_site)
    time.sleep(1)
    el1 = driver.find_element_by_xpath('/html/body/section/div/section/div/div/section/form/div[2]/div/button')
    el1.click()
    print('1. авторизовался')

    # сформировать
    el2 = driver.find_element_by_xpath( '/html/body/section/div/section[2]/div/div/section/section/div[2]/div[3]/span/div[2]/div[7]/div')
    el2.click()
    time.sleep(2)
    # сформировать
    el3 = driver.find_element_by_xpath(
        '/html/body/section/div/section[2]/div/div/section/section/div/div/div[5]/button')
    el3.click()



    # фильтр вида компании
    el4 = driver.find_element_by_xpath(
        '/html/body/section/div/section[2]/div/div/section/section/div/div[1]/div/div/div/div/div[1]/input')
    el4.click()
    time.sleep(1)
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("ENTER")
    time.sleep(1)
    print('4. исходящие')



    # сформировать
    el5 = driver.find_element_by_xpath(
        '/html/body/section/div/section[2]/div/div/section/section/div/div[2]/div[3]/span/div[1]/div[5]/div[1]/i')
    el5.click()


    time.sleep(5)
    driver.quit()


    def move_file():
        shutil.move(search_file(),  f'{new_place}\\111.xls')

site_evning()