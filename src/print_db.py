import pandas as pd
import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute(""" CREATE TABLE Users(
    User_ID integer PRIMARY KEY,
    Username text,
    Email text,
    Password text
    )""")

#  for i in range(10):
 #  conn.cursor().execute(f" INSERT INTO Users VALUES ({i}, 'Username{i}', 'Password{i}')")

#  c.execute("DELETE FROM Users")

conn.commit()

print(pd.read_sql_query("SELECT * FROM Users", conn))

conn.close()
