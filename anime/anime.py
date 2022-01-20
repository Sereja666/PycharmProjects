import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

# зайти на сайт
user_name = "Sereja666"
password = "Z2366212z"
driver = webdriver.Chrome()
driver.get("https://tr.anidub.com/anime_tv/anime_ongoing/11282-boku.html")
element = driver.find_element_by_id("login_name")
element.send_keys(user_name)
element = driver.find_element_by_id("login_password")
element.send_keys(password)
element.send_keys(Keys.RETURN)
# element.close()

# найти название аниме
element_titl = driver.find_element_by_id("news-title")
text_titl = element_titl.text

# записать его в лог


# найти номер серии аниме
number_anime = re.findall('\[([^$]*)\]', text_titl)
number_anime = number_anime[0]
n = number_anime[:2]

with open('log_anime.txt', 'w') as f:
    f.write(number_anime[0])
    f.write(n)



print(element_titl.text)
element_torrent = driver.find_element_by_link_text('<a href="/engine/download.php?id=32598" class=" "><span class="">Скачать торрент!</span></a>')
