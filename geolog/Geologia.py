import pandas as pd
import numpy as np

df = pd.read_excel('Приложение Ж.xlsx', sheet_name='Белая', header=[0, 1, 2] )
n = 8
#
# for index, value in df.iteritems():
#     print( index)
df.drop(df.tail(n).index, axis=0,inplace=True) # drop last n rows
'''
свыше 10 мм      А10       NaN
10 - 5 мм        А5        NaN
5 - 2 мм         А2        NaN
2 - 1 мм         А1        NaN
1 - 0,5 мм       А0,5      NaN
0,5 - 0,25 мм    А0,25     NaN
0,25 - 0,10 мм   А0,1      NaN
0,10 - 0,05 мм   А0,05     NaN
0,05 - 0,01 мм   А0,01     NaN
0,01 - 0,002 мм  А0,002    NaN
меньше 0,002 мм  А0        NaN
'''
# print(df.iloc[1]['Содержание частиц, %'])
df['Содержание частиц, %'] = df['Содержание частиц, %'].fillna(0).astype(int)
for index, value in df.iterrows():

    print(value['Содержание частиц, %'].sum(axis=0))
    df.loc[index, 'это 100?'] = value['Содержание частиц, %'].sum(axis=0)

print(df.to_string())