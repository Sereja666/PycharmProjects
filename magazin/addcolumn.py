import sqlite3

conn = sqlite3.connect("TV_price.db")
cur = conn.cursor()


cur.execute("ALTER table TV_price add column '07.05.2022' 'long'") # Add a column "WorkingID"
conn.commit()