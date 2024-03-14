

import requests

from magazin.models import TVModel, DataModel


# https://curlconverter.com/python/
cookies = {
    'current_path': 'c5f58b981d1ed0bad05ae63f54072ea9dcdf57acef965084aa1e42e07b47de20a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A133%3A%22%7B%22city%22%3A%22884019c7-cf52-11de-b72b-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041a%5Cu0440%5Cu0430%5Cu0441%5Cu043d%5Cu043e%5Cu0434%5Cu0430%5Cu0440%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
    'phonesIdent': 'e07ddea9bd03d9e4e40de8d8072203116666f24e071a2809ffdd88f5b4c76ef5a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%229cea1409-fbe0-4646-9f80-82f64cb9768e%22%3B%7D',
    'cartUserCookieIdent_v3': '4bfd910a8cf2212ca39311668c7da47ce9f9e6ee90944b606378be1eef83b11ba%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22c595e84c-e372-34c4-b9b8-f7a89246de3d%22%3B%7D',
    'auth_public_uid': '2121754422d3cdde7902edcbe38e9459',
    'date-user-last-order-v2': 'd66b611c2469935985ffaf3f4f3ee4e1af4cbb0057deed236b721b077df63da3a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A1686218470%3B%7D',
    '_ab_': '%7B%22search-sandbox%22%3A%22default%22%7D',
    'PHPSESSID': '57c69f0b9ca860e714702386ef9fcf5c',
    'lang': 'ru',
    '_csrf': '030f1d7ae4924a6047a1c5856acf1718f7f5a5f6699055a0ba4b15c5c8a423d1a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22mYMi9FLKOQdGIFsQaDCFHiKOJGNjKKY7%22%3B%7D',
    'city_path': 'krasnodar',
    'qrator_jsr': '1702318574.298.RDoNeJgedOwcdMxj-ec7emamniot6le26sntsu470lrurnl6j-00',
    'qrator_ssid': '1702318574.753.kf4aOhxjGCNIGJMf-85geket1kircclv7gc061fei9i8u3hjj',
    'qrator_jsid': '1702318574.298.RDoNeJgedOwcdMxj-jklcsosn1tthi3kejjntd2r4pvptg32n',
    'auth_access_token': 'eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoU1NJRCI6IjU3ZjA0ZWFiZTg1MzBmMjE4YWYyODIxM2Q4NWU1ZDhhMWQwM2Y3ODY3MTU5NTUwNTk4NmU0ZGEyNTM4ZDc3NjIiLCJleHAiOjE3MDIzMTk0NzYsInJuZCI6ImQwMGE1YTc4YWI0MjBiMzM3NjUxZGVhNTZjMDI5NjE2YzdkNDI2YzBjMGQyOWRkOGJhZTZiOGIxM2M0ZGQxZjQiLCJ1c2VySWQiOiJjZTBmMWRiNS0wNmVmLTk3Y2MtZTFjMi1lNTc5YWI2MTYxMWUiLCJ1c2VyTmFtZSI6IiJ9.MEUCIQC5KEMAq57FTrTxBIQ1cFSHyirHZk3WtTI56PzpRO2SEAIgK-ODDiS9l1ARvS5ibR1rI5xSw1oIsVA5HcqTbPfBwkg',
    'auth_refresh_token': 'fe9802956efa3def9eb1a4c191a9681c5b028e32f5f675252d45267971ded7a8',
    'auth_ssid': '57f04eabe8530f218af28213d85e5d8a1d03f78671595505986e4da2538d7762',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.dns-shop.ru/catalog/17a8ae4916404e77/televizory/no-referrer',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-Token': 'p6m59GR-0fDog17tfVOwoyYttzrQ-shL_r-Kxkx05WbK8PSdXTidu6fSOqo0FcPyR2n0fJiTgwS0-MSsBz-8UQ==',
    'Origin': 'https://www.dns-shop.ru',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Connection': 'keep-alive',
    # 'Cookie': 'current_path=c5f58b981d1ed0bad05ae63f54072ea9dcdf57acef965084aa1e42e07b47de20a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A133%3A%22%7B%22city%22%3A%22884019c7-cf52-11de-b72b-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041a%5Cu0440%5Cu0430%5Cu0441%5Cu043d%5Cu043e%5Cu0434%5Cu0430%5Cu0440%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; phonesIdent=e07ddea9bd03d9e4e40de8d8072203116666f24e071a2809ffdd88f5b4c76ef5a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%229cea1409-fbe0-4646-9f80-82f64cb9768e%22%3B%7D; cartUserCookieIdent_v3=4bfd910a8cf2212ca39311668c7da47ce9f9e6ee90944b606378be1eef83b11ba%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22c595e84c-e372-34c4-b9b8-f7a89246de3d%22%3B%7D; auth_public_uid=2121754422d3cdde7902edcbe38e9459; date-user-last-order-v2=d66b611c2469935985ffaf3f4f3ee4e1af4cbb0057deed236b721b077df63da3a%3A2%3A%7Bi%3A0%3Bs%3A23%3A%22date-user-last-order-v2%22%3Bi%3A1%3Bi%3A1686218470%3B%7D; _ab_=%7B%22search-sandbox%22%3A%22default%22%7D; PHPSESSID=57c69f0b9ca860e714702386ef9fcf5c; lang=ru; _csrf=030f1d7ae4924a6047a1c5856acf1718f7f5a5f6699055a0ba4b15c5c8a423d1a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22mYMi9FLKOQdGIFsQaDCFHiKOJGNjKKY7%22%3B%7D; city_path=krasnodar; qrator_jsr=1702318574.298.RDoNeJgedOwcdMxj-ec7emamniot6le26sntsu470lrurnl6j-00; qrator_ssid=1702318574.753.kf4aOhxjGCNIGJMf-85geket1kircclv7gc061fei9i8u3hjj; qrator_jsid=1702318574.298.RDoNeJgedOwcdMxj-jklcsosn1tthi3kejjntd2r4pvptg32n; auth_access_token=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoU1NJRCI6IjU3ZjA0ZWFiZTg1MzBmMjE4YWYyODIxM2Q4NWU1ZDhhMWQwM2Y3ODY3MTU5NTUwNTk4NmU0ZGEyNTM4ZDc3NjIiLCJleHAiOjE3MDIzMTk0NzYsInJuZCI6ImQwMGE1YTc4YWI0MjBiMzM3NjUxZGVhNTZjMDI5NjE2YzdkNDI2YzBjMGQyOWRkOGJhZTZiOGIxM2M0ZGQxZjQiLCJ1c2VySWQiOiJjZTBmMWRiNS0wNmVmLTk3Y2MtZTFjMi1lNTc5YWI2MTYxMWUiLCJ1c2VyTmFtZSI6IiJ9.MEUCIQC5KEMAq57FTrTxBIQ1cFSHyirHZk3WtTI56PzpRO2SEAIgK-ODDiS9l1ARvS5ibR1rI5xSw1oIsVA5HcqTbPfBwkg; auth_refresh_token=fe9802956efa3def9eb1a4c191a9681c5b028e32f5f675252d45267971ded7a8; auth_ssid=57f04eabe8530f218af28213d85e5d8a1d03f78671595505986e4da2538d7762',
}

data = 'data={"type":"product-buy","containers":[{"id":"as-69pkN0","data":{"id":"5331498"}},{"id":"as-pZEGr9","data":{"id":"5401378"}},{"id":"as-eLP52p","data":{"id":"5401387"}},{"id":"as-UfX2Rx","data":{"id":"5042201"}},{"id":"as-WU2czu","data":{"id":"8142432"}},{"id":"as--b1-RL","data":{"id":"5401382"}},{"id":"as-KJvpOM","data":{"id":"5401389"}},{"id":"as-zWT2WT","data":{"id":"4891643"}},{"id":"as-XH6VHY","data":{"id":"9967282"}},{"id":"as-fuB0z-","data":{"id":"5401379"}},{"id":"as-_FSqLV","data":{"id":"4895755"}},{"id":"as-uF1FTF","data":{"id":"5401380"}},{"id":"as-6gqlqe","data":{"id":"5068930"}},{"id":"as-7xR8lM","data":{"id":"5308764"}},{"id":"as-Xs5xOr","data":{"id":"1645638"}},{"id":"as-nkJoL1","data":{"id":"5042232"}},{"id":"as-Z__1KE","data":{"id":"5359835"}},{"id":"as-aFIQ_H","data":{"id":"5401388"}}]}'




class ParseDNS:
    def __init__(self):
        pass

    def parser(self):
        response = requests.post('https://www.dns-shop.ru/ajax-state/product-buy/?p=2', cookies=cookies,
                                 headers=headers, data=data)
        print(response.json()['data']['states'])
        # items_info = Items().parse_obj(response.json()['data']['states'])
        # print(items_info.json)

        tv_model = TVModel(**response.json())
        data_model = DataModel(**tv_model.data)

        current_price = data_model.price['current']
        name = data_model.name

        print(current_price)  # Выводит: 6299
        print(name)


if __name__ == '__main__':
    parserDNS = ParseDNS()
    parserDNS.parser()