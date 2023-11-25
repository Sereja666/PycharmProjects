import csv
from telega import send_to_telega
import requests
import time
import datetime

import pandas as pd
from sql_tools import has_value, add_to_db, cursor
import configparser




day_now = datetime.datetime.now()

class VK_Robot:
    def __init__(self, domain, token):
        self.domain = domain
        self.token = token #Сервисный ключ доступа


    def act(self):
        self.take_posts()
        self.selection()
        self.push_to_db()
        time.sleep(1)


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
    token = config["service"]["vk_token"]

    for group in groups_list:
        robot = VK_Robot(group, token)
        robot.act()
