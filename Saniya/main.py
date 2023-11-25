import socket
import pandas as pd

df = pd.DataFrame(columns=['name', 'ip'])


def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.error:
        return None

with open('comp_list.txt') as file:
    for name in file.readlines():
        name = name.replace('\n', '')

        ip_address = get_ip_address(name)

        if ip_address:
            new_row = {'name': name, 'ip': ip_address}

        else:
            new_row = {'name': name, 'ip': "не найден"}
        df = df._append(new_row, ignore_index=True)


df.to_excel("finish.xlsx")
