import socket
import pandas as pd

df_hosts = pd.read_excel(r'C:\Python\PycharmProjects\Saniya\pcheck.xlsx', sheet_name="checkdns")
# print(df_hosts.head().to_string())
df_new = pd.DataFrame(columns=['name', 'ip'])


def get_ip(host: str):
    try:
        ip_list = []
        ais = socket.getaddrinfo(host,0,0,0,0)
        for result in ais:
            ip_list.append(result[-1][0])
            ip_list = list(set(ip_list))
        return ip_list
    except socket.gaierror as err:
        return f'ошибка -> {err}'


for index, row in df_hosts.iterrows():
    df_new.loc[ len(df_new.index )] = [row['Name'],    get_ip(row['Name'])]


# print(df_new.head().to_string())
df_new.to_excel('result.xlsx')



# ip_list = []
# ais = socket.getaddrinfo("cdn.ngenix.net",0,0,0,0)
# for result in ais:
#     ip_list.append(result[-1][0])
#     ip_list = list(set(ip_list))
# print(ip_list)