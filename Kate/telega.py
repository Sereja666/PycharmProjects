
from datetime import datetime


import requests

def send_to_telega(resurs , name, news, day_data, token):
    chat_id = "-805580491"


    message = f'''**{resurs}**
    {name} {day_data} 
    
    {news}'''
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # Эта строка отсылает сообщение