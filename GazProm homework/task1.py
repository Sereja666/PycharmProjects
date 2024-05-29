"""
Есть таблица table1 с колонками id и datatime. Напишите запрос, который вернёт максимальное значение id и значение даты для этого id
"""

SELECT id, datatime
FROM table1
WHERE id = (SELECT MAX(id) FROM table1)


SELECT id, datatime
FROM table1
ORDER BY id DESC
LIMIT 1


SELECT t1.id, t1.datatime
FROM table1 t1
JOIN (SELECT MAX(id) as max_id FROM table1) t2
ON t1.id = t2.max_id


import pandas as pd

# Создание DataFrame table1 (пример данных)
data = {'id': [1, 2, 3, 4, 5],
        'datatime': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05']}
table1 = pd.DataFrame(data)

# Нахождение максимального значения id и соответствующей даты
max_id = table1['id'].max()
result = table1[table1['id'] == max_id][['id', 'datatime']]
print(result)

"""
В базе данных создана таблица account_turn с оборотами (turn) по счетам (account_id). Каждый счет имеет одну запись за дату data
account_id      data            turn
1	       "2019-01-01"	        100
2	       "2019-01-01"	        200
2	       "2019-01-03"	        300
2	       "2019-01-07"	        200
3	       "2019-01-03"	        200
3	       "2019-01-06"	        600
3	       "2019-01-04"	        200
4	       "2019-01-05"	        500
Требуется посчитать остаток за каждый день с нарастающим итогом
account_id      data            turn    rest
1	       "2019-01-01"	        100     100
2	       "2019-01-01"	        200     200
2	       "2019-01-03"	        300     500
2	       "2019-01-07"	        200     700
3	       "2019-01-03"	        200     200
3	       "2019-01-06"	        600     400
3	       "2019-01-04"	        200     1000
4	       "2019-01-05"	        500     500
"""