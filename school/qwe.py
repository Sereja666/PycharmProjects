import os

import requests, lxml
import  pars_school
# send=requests.post('https://solncesvet.ru/content/kurs') #делаем запрос

import requests
from bs4 import BeautifulSoup

url = 'https://solncesvet.ru/content/kurs'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('a')
list_folder = []
for title in quotes:
    end_path = title.text.strip().replace('/', '')
    if end_path.isdigit():
        list_folder.append(end_path)
    # if ".rar" in title.get('href'):
    #     print(title.get('href'))

        # pars_school.download_file(title.get('href'))
print(list_folder)


def search_files(rashirenie):
    if rashirenie in title.get('href'):
        url2 = rf"https://solncesvet.ru/content/kurs/{folder}/{title.get('href')}"
        print(url2)
        folder_out = rf"C:\PyTest\Любовь\kurs\{folder}"
        try:
            os.mkdir(folder_out)
        except FileExistsError:
            pass
        if title.text is None:
            file_name = f'ahrhiv_{folder}_{i}{rashirenie}'
        else:
            file_name = title.text
        pars_school.download_file(url2, folder_out, file_name)

for folder in list_folder:
    url1 = f'https://solncesvet.ru/content/kurs/{folder}/'

    response1 = requests.get(url1)
    soup1 = BeautifulSoup(response1.text, 'lxml')
    quotes1 = soup1.find_all('a')
    i = 0
    for title in quotes1:
        search_files(".rar")
        search_files(".zip")
        search_files(".jpg")
        search_files(".png")
        search_files(".docx")
        search_files(".doc")
        i+=1


# print('+++++++++++++++++++++++++++++++')
# for title in quotes:
#     end_path = title.text.strip().replace('/', '')
#     if end_path.isdigit():
#         url1 = f'https://solncesvet.ru/content/kurs/{end_path}/'
#         response1 = requests.get(url1)
#         soup1 = BeautifulSoup(response.text, 'lxml')
#         quotes1 = soup1.find_all('a')
#         for title in quotes:
#             if ".rar" in title.get('href'):
#                 print(f"{end_path}     ---   {title.get('href')}")
#                 # pars_school.download_file(title.get('href'))