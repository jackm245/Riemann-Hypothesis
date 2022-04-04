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


def database_insert(table, *args):

    """
    database_insert inserts the arguments into a desired table in the database
    """

    query = f"INSERT INTO {table} VALUES ({', '.join('?' for _ in args)})"
    database_query(query, *args)


def database_query(query, *args, database='database.db'):

    """
    database_query takes in a query as an input, and executes it on the database
    This allows the database to be queried from any point in the program without
    having to pass a database variable into every function, or by using a global
    variable
    """

    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(query, args)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return rows


def database_print():
    print('='*16)
    print('=   DATABASE   =')
    print('='*16)
    tables = [table[0] for table in database_query("""SELECT name FROM sqlite_master
    WHERE type='table'""")]
    for table in tables:
        name = f"- Table: {table} -"
        border = '-' * len(name)
        print(f'{border}\n{name}\n{border}')
        print(', '.join([column[1] for column in database_query(f"PRAGMA table_info({table})")]))
        rows = database_select(['*'], [table])
        for row in rows:
            print(row)
    print('=' * 20)


def create_users_table():

    """ Create the Users table in the database """

    database_query(""" CREATE TABLE Users(
    Username text PRIMARY KEY,
    Email text,
    Password text
    )""")

def create_correct_answers_table(questions_and_answers):

    """ Create the Answers table in the database """

    database_query(""" CREATE TABLE CorrectAnswers(
    Question_No integer,
    CorrectAnswer text,
    PRIMARY KEY (Question_No, CorrectAnswer)
    )""")
    for question_no, dict in enumerate(questions_and_answers):
        for answer in dict["Answers"]:
            database_insert('CorrectAnswers', question_no, answer)


def create_questions_table(questions_and_answers):

    """ Create the Questions table in the database """

    database_query(""" CREATE TABLE Questions(
    Question_No integer PRIMARY KEY,
    Question text
    )""")
    for question_no, dict in enumerate(questions_and_answers):
        database_insert('Questions', question_no, dict["Question"])


def create_user_answer_table():

    """ Create the User Answer table in the database """

    database_query(""" CREATE TABLE UsersAnswers(
    Question_No integer,
    Username integer,
    UsersAnswer integer,
    PRIMARY KEY (Question_No, Username)
    )""")


def create_notes_table():

    """ Create the Notes table in the database """

    database_query(""" CREATE TABLE Notes(
    Username integer,
    Section text,
    Text text,
    PRIMARY KEY (Username, Section)
    )""")


def create_zeta_table():

    """ Create the Zeta table in the database """

    database_query(""" CREATE TABLE Zeta(
    Zeta_ID integer PRIMARY KEY,
    Input_Real REAL,
    Input_Imag REAL,
    Output_Real REAL,
    Output_imag REAL
    )""")


def create_user_zeta_table():

    """ Create the User Zeta table in the database """

    database_query(""" CREATE TABLE UserZeta(
    Zeta_ID integer,
    Username integer,
    PRIMARY KEY (Zeta_ID, Username)
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
    Zero_ID integer,
    Username integer,
    PRIMARY KEY (Zero_ID, Username)
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

    if not os.path.isfile(database):
        touch(database)
        QUESTIONS_AND_ANSWERS = [
        {'Question': 'Error',
            'Answers': ['Error']},
        {'Question': 'What is the name of this program? Visualising the ___ Hypothesis',
            'Answers': ['Riemann']},
        {'Question': 'What is 1+1?',
            'Answers': ['2', 'Two']},
        {'Question': 'Which character is used to denote the imaginary unit?',
            'Answers': ['i', 'j']},
        {'Question': 'What is one practical appication of the Riemann Hypothesis?',
            'Answers': ['Cryptography', 'Quantum Physics', 'Prime Numbers']},
        {'Question': 'What is the value of the first non-trivial zeta zero?',
            'Answers': ['14.1', '0.5+14.1i', '0.5 + 14.1i', '0.5+14.1j', '0.5 + 14.1j']},
        {'Question': 'What is hypothesised to be the real part of every non-trivial zero of the riemann zeta function?',
            'Answers': ['0.5', '1/2']},
        {'Question': 'What is the value of ζ(5+5i)',
            'Answers': ['0.974+0.012i', '0.974+0.012j']},
        {'Question': 'What prize would you get from the Clay Mathematics Institute if you managed to prove the Riemann Hypothesis?',
            'Answers': ['$1000000', '$1,000,000', 'One Million Dollars', 'A Million Dollars']},
        {'Question': 'What is the name of Riemann\'s 1859 paper where he first conjectured the Riemann Hypothesis?',
            'Answers': ['On The Number Of Primes Less Than a Given Magnitude']},
        {'Question': 'What type of numbers would proving the Riemann Hypothesis have an impact over?',
            'Answers': ['Prime Numbers', 'Primes', 'Prime']}
        ]
        create_users_table()
        create_correct_answers_table(QUESTIONS_AND_ANSWERS)
        create_questions_table(QUESTIONS_AND_ANSWERS)
        create_user_answer_table()
        create_notes_table()
        create_zeta_table()
        create_user_zeta_table()
        create_zeroes_table()
        create_user_zeroes_table()


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


database_print()
