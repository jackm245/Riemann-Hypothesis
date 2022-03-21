"""
database_functions.py
=====================

Contains subroutines that are used to query and interact with SQL databases

These subroutines include:
    - database_select
    - database_insert
    - database_query
"""

import pandas as pd
import sqlite3
import os
from file_handling import touch, remove


def database_select(headings, tables):

    """
    database_select takes in a list of heading and tables as inputs, and returns
    the query from selecting these from the SQL database
    """

    query = f"SELECT {', '.join(headings)} FROM {', '.join(tables)}"
    return database_query(query)


def database_insert(table, values):

    """
    database_insert inserts the paramter values into a desired table in the database
    """

    query = f"INSERT INTO {table} VALUES ({', '.join('?' for _ in values)})"
    database_query(query, values)


def database_query(query, values=[], database='database.db'):

    """
    database_query takes in a query as an input, and executes it on the database
    This allows the database to be queried from any point in the program without
    having to pass a database variable into every function, or by using a global
    variable
    """

    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(query, values)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


# delete when done and remove where imported
def database_print():
    print('-------------')
    print("Table: Users")
    print('-------------')
    table = database_select(['*'], ['Users'])
    for row in table:
        print(row)


def create_users_table():
    database_query(""" CREATE TABLE Users(
    User_ID integer PRIMARY KEY,
    Username text,
    Email text,
    Password text
    )""")

def create_questions_table():
    database_query(""" CREATE TABLE Questions(
    Question_ID integer PRIMARY KEY,
    Question_No integer,
    Question text,
    Answer text
    )""")


def create_answers_table():
    pass


def create_database(database='database.db'):
    touch(database)
    create_users_table()
    create_questions_table()


def delete_database(database='database.db'):
    remove(database)


def reset_database(database='database.db''):
    delete_database()
    create_database()
