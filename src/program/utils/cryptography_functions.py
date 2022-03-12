import argon2
from argon2 import PasswordHasher as ph


def get_pepper():
    return 'Sr4QkXyIhv4SiijxAWxU'


def hash_password(password):
    hash = ph().hash(get_pepper() + password)
    return hash


def check_password(password, hash):
    try:
        valid =  ph().verify(hash, get_pepper() + password)
    except argon2.exceptions.VerifyMismatchError:
        return False
    else:
        return True
