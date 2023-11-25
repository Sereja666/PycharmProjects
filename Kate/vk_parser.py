import csv
import os

from telega import send_to_telega
import requests
import time
import datetime

import pandas as pd
from sql_tools import has_value, add_to_db, create_table
import configparser


import sqlite3


conn = sqlite3.connect("news.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

create_table()


day_now = datetime.datetime.now()

class VK_Robot:
    def __init__(self, domain, config):
        self.domain = domain
        self.config = config

    def act(self):
        self.read_config()
        self.take_posts()
        self.selection()
        self.push_to_db()
        time.sleep(1)

    def read_config(self):
        self.token = self.config["service"]["vk_token"]
        self.telegram_token = self.config["service"]["telegram_token"]

    def convert_time(self, data):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data))
    def take_posts(self):

        version = 5.92
        offset = 0
        all_post = []

        while offset < 3:
            response = requests.get('https://api.vk.com/method/wall.get', params={
                'access_token' : self.token,
                'v' : version,
                'domain' : self.domain,
                'count' : 1,
                'offset' : offset
            })
            data = response.json()['response']['items']
            offset+=1
            all_post.extend(data)
            time.sleep(0.5)
        return all_post

    def selection(self):
        self.df = pd.DataFrame(columns=[ 'name', 'news', 'news_data'])
        all_p = self.take_posts()
        i = 0
        for post in all_p:
            # attachments title , text, date
            for key, value in post.items():
                if value:
                    if post["text"]:

                        self.df.loc[i] = [f'news_{post["date"]}', post["text"], self.convert_time(post["date"]) ]


                if key == 'copy_history':  # если это репост
                    self.df.loc[i] = [f'news_', value[0]['text'], self.convert_time(post["date"])]

                i += 1


    def push_to_db(self):
        for index, value in self.df.iterrows():
            # cursor, table, column, value
            if has_value(cursor, 'news_table', 'news', value["news"]):
                print('новость была уже')

            else:
                add_to_db(resurs=self.domain , name=self.df.loc[index]["name"], news=self.df.loc[index]["news"], day_data=self.df.loc[index]["news_data"])

                send_to_telega(resurs=self.domain , name=value["name"], news=value["news"], day_data=value["news_data"], token=self.telegram_token)
                print('добавлена новая новость')


#
if __name__ == '__main__':
    os.chdir(os.path.abspath(os.curdir))
    config = configparser.ConfigParser()
    config.read('config.ini')
    groups_list = config["vk_groups"]["vk_groups"]
    groups_list = groups_list.split('; ')

    for group in groups_list:
        robot = VK_Robot(group, config)
        robot.act()
