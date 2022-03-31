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
    print('='*12)
    print('= DATABASE =')
    print('='*12)
    tables = [table[0] for table in database_query("""SELECT name FROM sqlite_master
    WHERE type='table';""")]
    for table in tables:
        name = f"- Table: {table} -"
        border = '-' * len(name)
        print(f'{border}\n{name}\n{border}')
        print(', '.join([column[1] for column in database_query(f"PRAGMA table_info({table})")]))
        rows = database_select(['*'], [table])
        for row in rows:
            print(row)
    print('=' * 20)
    print(tables)


def create_users_table():

    """ Create the Users table in the database """

    database_query(""" CREATE TABLE Users(
    User_ID integer PRIMARY KEY,
    Username text,
    Email text,
    Password text
    )""")

def create_answers_table(questions_and_answers):

    """ Create the Answers table in the database """

    database_query(""" CREATE TABLE Answers(
    Answer_ID integer PRIMARY KEY,
    Answer text
    )""")

    for answer_id, (question, answer) in enumerate(questions_and_answers):
        database_insert('Answers', [answer_id, answer])


def create_questions_table(questions_and_answers):

    """ Create the Questions table in the database """

    database_query(""" CREATE TABLE Questions(
    Question_ID integer PRIMARY KEY,
    Question text,
    Answer_ID integer
    )""")
    for question_id, (question, answer) in enumerate(questions_and_answers):
        answer_id = database_query("SELECT Answer_ID FROM Answers WHERE Answer=?", [answer])[0][0]
        database_insert('Questions', [question_id, question, answer_id])


def create_user_answer_table():

    """ Create the User Answer table in the database """

    database_query(""" CREATE TABLE UserAnswer(
    User_ID integer,
    Question_ID integer,
    Answer_ID integer
    )""")


def create_notes_table():

    """ Create the Notes table in the database """

    database_query(""" CREATE TABLE Notes(
    Note_ID integer PRIMARY KEY,
    Section text,
    Text text,
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


def delete_table(table):
    try:
        database_query(f"DROP TABLE IF EXISTS {table}")
    except sqlite3.OperationalError as error:
        print(error)


def create_database(database='database.db'):

    """
    Create the database and all of the tables
    If it doesnt already exist
    """

    if not os.path.isfile('database.db'):
        questions_and_answers = [
        ('Error', 'Error'),
        ('What is the name of this program?<br>Visualising the ___ Hypothesis', 'Riemann'),
        ('What is 1+1?', '2'),
        ('What character is used to denote the imaginary unit?', 'i')
        ]
        touch(database)
        create_users_table()
        create_answers_table(questions_and_answers)
        create_questions_table(questions_and_answers)
        create_user_answer_table()
        create_notes_table()
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


questions_and_answers = [
('Error', 'Error'),
('What is the name of this program?<br>Visualising the ___ Hypothesis', 'Riemann'),
('What is 1+1?', '2'),
('What character is used to denote the imaginary unit?', 'i')
]
delete_table('Answers')
delete_table('Questions')
create_answers_table(questions_and_answers)
create_questions_table(questions_and_answers)
database_print()
