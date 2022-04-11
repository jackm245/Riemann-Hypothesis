"""
cryptography_functions.py
=========================

Contains subroutines that are used for encyption and hashing

These subroutines include:
    - get_pepper
    - hash_password
    - check_password

Objectives completed in this file:
    2(c)
"""


import argon2
from argon2 import PasswordHasher as ph


def get_pepper():

    """
    Returns the value of the pepper that is used in this program to help
    secure the hashes in the database
    """

    return 'Sr4QkXyIhv4SiijxAWxU'


def hash_password(password):

    """
    Takes in a password as a parameter and returns the hashed version of this
    password using the pepper and the argon2 encryption algorithm
    """

    hash = ph().hash(get_pepper() + password)
    return hash


def check_password(password, hash):

    """
    Used to check whether a given hash is the hashed version of a password

    Because hashing cannot be undone to check whether the hash is the same as a
    password, it is required that the password is hashed, and if this hash is the
    same as the one we are comparing it to, then the passwords are the same.
    """

    try:
        valid =  ph().verify(hash, get_pepper() + password)
    except argon2.exceptions.VerifyMismatchError:
        return False
    else:
        return True
