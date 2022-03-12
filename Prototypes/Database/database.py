import sqlite3

conn = sqlite3.connect('sqldatabase.db')

c = conn.cursor()

c.execute(""" CREATE TABLE customers(
    first_name text,
    last_name text
    )""")

conn.commit()

conn.close()
