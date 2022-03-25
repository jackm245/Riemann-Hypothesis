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
from .file_handling import touch, remove


__all__ = ['database_select', 'database_insert', 'database_query',
        'create_database', 'reset_database', 'get_user_id', 'get_zeta_id',
        'database_print']


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


def database_print():
    tables = [table[0] for table in database_query("""SELECT name FROM sqlite_master
    WHERE type='table';""")]
    for table in tables:
        name = f"- Table: {table} -"
        border = '-' * len(name)
        print(border)
        print(name)
        print(border)
        rows = database_select(['*'], [table])
        for row in rows:
            print(row)


def create_users_table():

    """ Create the Users table in the database """

    database_query(""" CREATE TABLE Users(
    User_ID integer PRIMARY KEY,
    Username text,
    Email text,
    Password text
    )""")


def create_questions_table():

    """ Create the Questions table in the database """

    database_query(""" CREATE TABLE Questions(
    Question_ID integer PRIMARY KEY,
    Question_No integer,
    Question text,
    Answer text
    )""")


def create_answers_table():

    """ Create the Answers table in the database """

    database_query(""" CREATE TABLE Answers(
    Answer_ID integer PRIMARY KEY,
    Answer text,
    Question_ID integer
    )""")


def create_user_answer_table():

    """ Create the User Answer table in the database """

    database_query(""" CREATE TABLE UserAnswer(
    User_ID integer PRIMARY KEY,
    Answer_ID integer
    )""")


def create_notes_table():

    """ Create the Notes table in the database """

    database_query(""" CREATE TABLE Notes(
    Notes_ID integer PRIMARY KEY,
    Note_No integer,
    Question text
    )""")


def create_responses_table():

    """ Create the Responses table in the database """

    database_query(""" CREATE TABLE Responses(
    Responses_ID integer PRIMARY KEY,
    Notes_ID integer,
    Response string,
    User_ID integer
    )""")


def create_zeta_table():

    """ Create the Zeta table in the database """

    database_query(""" CREATE TABLE Zeta(
    Zeta_ID integer PRIMARY KEY,
    Input text,
    Output text
    )""")


def create_user_zeta_table():

    """ Create the User Zeta table in the database """

    database_query(""" CREATE TABLE UserZeta(
    Zeta_ID integer PRIMARY KEY,
    User_ID integer
    )""")


def create_zeroes_table():

    """ Create the Zeroes table in the database """

    database_query(""" CREATE TABLE Zeroes(
    Zero_ID integer PRIMARY KEY,
    Zero_Real_Input real,
    Zero_Imag_Input real
    )""")


def create_user_zeroes_table():

    """ Create the User Zeta Zeroes table in the database """

    database_query(""" CREATE TABLE UserZeroes(
    Zero_ID integer PRIMARY KEY,
    User_ID integer
    )""")


def create_database(database='database.db'):

    """
    Create the database and all of the tables
    If it doesnt already exist
    """

    if not os.path.isfile('database.db'):
        touch(database)
        create_users_table()
        create_questions_table()
        create_answers_table()
        create_user_answer_table()
        create_notes_table()
        create_responses_table()
        create_zeta_table()
        create_user_zeta_table()
        create_zeta_zeroes_table()
        create_user_zeta_zeroes_table()


def delete_database(database='database.db'):

    """ remove the database file, thus deleting the database """

    remove(database)


def reset_database(database='database.db'):

    """ clear all of the data from inside the database """

    delete_database()
    create_database()


def get_next_id(IDs, ID=0):
    if ID not in IDs:
        return ID
    else:
        return get_next_id(IDs, ID+1)

def get_id(ID, table):
    selection = database_select([ID], [table])
    IDs = set([row[0] for row in selection])
    ID_Number = get_next_id(IDs)
    return ID_Number


#  def get_user_id():
    #  selection = database_select(['User_ID'], ['Users'])
    #  User_IDs = set([row[0] for row in selection])
    #  User_ID = get_next_id(User_IDs)
    #  return User_ID


#  def get_zeta_id():
    #  selection = database_select(['Zeta_ID'], ['Zeta'])
    #  Zeta_IDs = set([row[0] for row in selection])
    #  Zeta_ID = get_next_id(Zeta_IDs)
    #  return Zeta_ID


#  def get_zeta_zero_id():
    #  selection = database_select(['Zeta_Zero_ID'], ['ZetaZero'])
    #  Zeta_Zero_IDs = set([row[0] for row in selection])
    #  Zeta_ID = get_next_id(Zeta_IDs)
    #  return Zeta_ID

# these can be improbed
# make 1 function where it tales what it wants as a paramter
#  database_query("DROP TABLE UserZetaZeroes")
#  database_query("DROP TABLE ZetaZeroes")

database_print()
