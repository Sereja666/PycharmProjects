import sqlite3


conn = sqlite3.connect("news.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
def create_table():
    try:
        # Создание таблицы
        cursor.execute("""
        CREATE TABLE news_table (
        resurs,
           name,
           news,
           day_data

);
    """)
    except sqlite3.OperationalError:
        pass

def add_to_db(resurs, name, news, day_data):
    # подготавливаем множественный запрос
    sql = 'INSERT INTO news_table (resurs, name, news, day_data) values(?, ?, ?, ?)'
    # указываем данные для запроса
    data = [
        (resurs, name, news, day_data),

    ]

    # добавляем с помощью множественного запроса все данные сразу
    with conn:
        conn.executemany(sql, data)

    # выводим содержимое таблицы на экран
    with conn:
        data = conn.execute("SELECT * FROM news_table")
        for row in data:
            print(row)

def has_value(cursor, table, column, value):
    query = 'SELECT * from {} WHERE {} = ? LIMIT 1'.format(table, column)
    return cursor.execute(query, (value,)).fetchone() is not None





# add_to_db(name='news1', news='буковки разныее',day_data='12.12.2202')

# if has_value(cursor, 'news_table', 'news', 'буковки'):
#     print('нашёл')
# else:
#     print('не нашёл')