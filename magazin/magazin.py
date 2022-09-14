import datetime

import requests
from bs4 import BeautifulSoup
import sqlite3


class Magazin:
    def __int__(self):
        pass

    def connectSQL(self):

        self.conn = sqlite3.connect("big_DB.db")  # или :memory: чтобы сохранить в RAM
        self.cursor = self.conn.cursor()
        try:
            # Создание таблицы
            self.cursor.execute("""CREATE TABLE Sitilink_TV_price
                              (name, price_data)
                           """)
        except sqlite3.OperationalError:
            pass

    def day_now(self):
        daynow = datetime.datetime.now()
        return daynow.strftime("%d.%m.%Y")

    def add_to_table(self, name, code ,price):
        self.cursor.execute(f"""INSERT INTO Sitilink_TV_price
                          VALUES ('{name}', {code} '{price}')"""
                       )

        # Сохраняем изменения
        self.conn.commit()


    def read_sitilink_TV(self):
        print("read_sitilink_TV")
        pages = ['']
        i = 2
        while i < 11:
            p = f'&p={i}'
            pages.append(p)
            i+=1
        for page in pages:
            url = f"https://www.citilink.ru/catalog/televizory/?view_type=list&f=discount.any%2Crating.any{page}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.find_all('a', class_='ProductCardHorizontal__title  Link js--Link Link_type_default')
            quotes_artikul = soup.find_all('div', class_='ProductCardHorizontal__vendor-code')
            quotes_cena = soup.find_all('span',
                                        class_='ProductCardVerticalPrice__price-current_current-price js--ProductCardVerticalPrice__price-current_current-price')

            for quote, code, priece in zip(quotes, quotes_artikul, quotes_cena):
                pr = priece.text.replace('\n','').replace(' ','')
                print(quote.text, code, pr)
                self.add_to_table(quote.text, code, pr)


    def act(self):
        self.day_now()
        self.connectSQL()
        self.read_sitilink_TV()

magazin = Magazin()
magazin.act()

