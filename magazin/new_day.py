import datetime
import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3


class Magazin:
    def __int__(self):
        pass

    def connectSQL(self):

        self.conn = sqlite3.connect("big_DB.db")  # или :memory: чтобы сохранить в RAM
        self.cursor = self.conn.cursor()


    def day_now(self):
        daynow = datetime.datetime.now()
        return daynow.strftime("%d.%m.%Y")


    def tempSQL(self):
        self.big_df = pd.read_sql('''SELECT * FROM  Sitilink_TV_price''', self.conn)

    def read_sitilink_TV(self):
        self.new_df = pd.DataFrame(columns=['name', self.day_now()])
        pages = ['']
        i1 = 2
        i = 0
        while i1 < 11:
            p = f'&p={i1}'
            pages.append(p)
            i1 += 1
        for page in pages:
            # url = f'https://www.citilink.ru/catalog/televizory/?view_type=grid&f=discount.any%2Crating.any{page}'
            url = f"https://www.citilink.ru/catalog/televizory/?view_type=list&f=discount.any%2Crating.any{page}"

            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            # quotes = soup.find_all('div', class_='ProductCardVertical__description')
            quotes = soup.find_all('a', class_='ProductCardHorizontal__title  Link js--Link Link_type_default')
            quotes_artikul = soup.find_all('div', class_='ProductCardHorizontal__vendor-code')
            quotes_cena = soup.find_all('span',
                                        class_='ProductCardVerticalPrice__price-current_current-price js--ProductCardVerticalPrice__price-current_current-price')




            for quote, code, priece in zip(quotes, quotes_artikul , quotes_cena):
                pr = priece.text.replace('\n', '').replace(' ', '')
                self.new_df.loc[i] = [quote.text, pr]
                i+=1
        print(self.new_df.to_string())
        try:
            self.big_df.drop(columns=['index'], axis=1, inplace=True)
        except KeyError:
            pass
        self.big_df = self.big_df.merge(self.new_df , left_on=["name"], right_on=['name'], how='outer')
        print('----------------------------------------')
        print(self.big_df.to_string())
        try:
            self.big_df.drop(columns=['index'], axis=1, inplace=True)
        except KeyError:
            pass
        self.big_df.to_sql('Sitilink_TV_price', con = self.conn, if_exists='replace')


    def percent(self, n1, n2):
        try:
            a = (int(n2) - int(n1)) / int(n2) * 100
            return a
        except ValueError:
            pass


    def comparison(self, i):
        name = self.big_df.loc[i][1]
        p1 = self.big_df.loc[i][-2]
        p2 = self.big_df.loc[i][-1]
        if p1 != p2:
            if self.percent(p2, p1) > 30:
                print(f'{name} {self.big_df.loc[i][0]} - {p1} - {p2}')

    def qqqq(self):
        for i, row in self.big_df.iterrows():
            try:
                self.comparison(i)
            except TypeError:
                pass


    def act(self):
        self.day_now()
        self.connectSQL()
        self.tempSQL()
        self.read_sitilink_TV()
        self.qqqq()


if __name__ == '__main__':
    magazin = Magazin()
    magazin.act()

