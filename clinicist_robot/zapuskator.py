# -*- coding: utf-8 -*-

import schedule
import time

from robot_morning import site
from robot_evning import site_evning
from config import start_call, start_download


def zapusk():
    schedule.every().monday.at(start_call).do(site)
    schedule.every().monday.at(start_download).do(site_evning)
    schedule.every().tuesday.at(start_call).do(site)
    schedule.every().tuesday.at(start_download).do(site_evning)
    schedule.every().wednesday.at(start_call).do(site)
    schedule.every().wednesday.at(start_download).do(site_evning)
    schedule.every().thursday.at(start_call).do(site)
    schedule.every().thursday.at(start_download).do(site_evning)
    schedule.every().friday.at(start_call).do(site)
    schedule.every().friday.at(start_download).do(site_evning)




    # нужно иметь свой цикл для запуска планировщика с периодом в 40 секунду:
    while True:
        schedule.run_pending()
        time.sleep(3)


if __name__ == '__main__':
    zapusk()