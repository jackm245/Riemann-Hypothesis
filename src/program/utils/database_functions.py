import pandas as pd
import sqlite3


def database_select(headings, tables):
    # for simple selection
    #  cur.execute("insert into lang values (?, ?)", ("C", 1972))
    #  query = f"INSERT INTO {table} VALUES ({', '.join('?' for _ in values)})"
    # SELECT * FROM Users WHERE
    query = f"SELECT {', '.join(headings)} FROM {', '.join(tables)}"
    return database_query(query)


def database_insert(table, values):
    #  cur.execute("insert into lang values (?, ?)", ("C", 1972))
    query = f"INSERT INTO {table} VALUES ({', '.join('?' for _ in values)})"
    database_query(query, values)


def database_query(query, values=[], database='database.db'):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(query, values)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows

#  print(database_query("DELETE FROM Users"))
#  print(database_select(['*'], ['Users']))
