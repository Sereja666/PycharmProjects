import csv
from telega import send_to_telega
import requests
import time
import datetime

import pandas as pd
from sql_tools import has_value, add_to_db, cursor
import configparser


import sqlite3


conn = sqlite3.connect("news.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
def create_table():
    try:
        # Создание таблицы
        cursor.execute("""
        CREATE TABLE news_table (
        resurs,
           name,
           news,
           day_data

);
    """)
    except sqlite3.OperationalError:
        pass

def add_to_db(resurs, name, news, day_data):
    # подготавливаем множественный запрос
    sql = 'INSERT INTO news_table (resurs, name, news, day_data) values(?, ?, ?, ?)'
    # указываем данные для запроса
    data = [
        (resurs, name, news, day_data),

    ]

    # добавляем с помощью множественного запроса все данные сразу
    with conn:
        conn.executemany(sql, data)

    # выводим содержимое таблицы на экран
    with conn:
        data = conn.execute("SELECT * FROM news_table")
        for row in data:
            print(row)

def has_value(cursor, table, column, value):
    query = 'SELECT * from {} WHERE {} = ? LIMIT 1'.format(table, column)
    return cursor.execute(query, (value,)).fetchone() is not None




create_table()
# add_to_db(name='news1', news='буковки разныее',day_data='12.12.2202')

# if has_value(cursor, 'news_table', 'news', 'буковки'):
#     print('нашёл')
# else:
#     print('не нашёл')




day_now = datetime.datetime.now()

class VK_Robot:
    def __init__(self, domain):
        self.domain = domain

    def act(self):
        self.take_posts()
        self.selection()
        self.push_to_db()
        time.sleep(1)


    def convert_time(self, data):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data))
    def take_posts(self):
        key = "kDbW9U3tUdmt1ttWIAH5" #Защищённый ключ
        token = "83d296bb83d296bb83d296bbe480c01e5e883d283d296bbe030c2ca6dbcf836bca82d41" #Сервисный ключ доступа
        version = 5.92
        offset = 0
        all_post = []

        while offset < 3:
            response = requests.get('https://api.vk.com/method/wall.get', params={
                'access_token' : token,
                'v' : version,
                'domain' : self.domain,
                'count' : 3,
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
        i_dict = 1
        i = 0
        for post in all_p:


            # attachments title , text, date
            for key, value in post.items():
                print(key, value)

                print(self.df.to_string())
                print(i)

                if value:

                    if post["text"]:
                        print('post["date"]', post["date"], 'post["text"] =',post["text"])
                        self.df.loc[i] = [f'news_{i_dict}', post["text"], self.convert_time(post["date"]) ]
                        i_dict += 1

                if key == 'copy_history':  # если это репост
                    print('нашёл copy_history')

                    print(value[0]['text'])

                    self.df.loc[i] = [f'news_', value[0]['text'], self.convert_time(post["date"])]
                    i_dict += 1
                i += 1



    def push_to_db(self):
        print(self.df.to_string())
        for index, value in self.df.iterrows():
            print(f'value["news"] - {self.df.loc[index]["news"]}, {type(value["news"])}')
            # cursor, table, column, value
            if has_value(cursor, 'news_table', 'news', value["news"]):
                print('новость была уже')

            else:
                add_to_db(resurs=self.domain , name=self.df.loc[index]["name"], news=self.df.loc[index]["news"], day_data=self.df.loc[index]["news_data"])

                send_to_telega(resurs=self.domain , name=value["name"], news=value["news"], day_data=value["news_data"])
                print('добавлена новая новость')


#
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    groups_list = config["vk_groups"]["vk_groups"]
    groups_list = groups_list.split('; ')

    for group in groups_list:
        robot = VK_Robot(group)
        robot.act()
#         #
#
#
# detbibkol_robot = VK_Robot('detbibkol')
# detbibkol_robot.act()
# #
# kdc_podvig = VK_Robot('kdc_podvig')
# kdc_podvig.act()
#
# id561283515 = VK_Robot('id561283515')
# id561283515.act()