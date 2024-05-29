
from datetime import datetime


import requests
TOKEN = "1111:1111"
def send_to_telega(resurs , name, news, day_data):
    chat_id = "-1111"


    message = f'''**{resurs}**
    {name} {day_data} 
    
    {news}'''
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # Эта строка отсылает сообщение

from datetime import datetime

import requests
TOKEN = "11111:1111"

def send_to_telega(chat_id, message):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())  # Эта строка отсылает сообщение


send_to_telega("-805580491", 'тут сообщение')
