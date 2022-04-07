"""
file_handling.py
================

Contains subroutines that are used to create and delete files

These subroutines include:
    - touch
    - remove
"""


import os


def touch(path):
    """ Create a file if it does not already exist """
    try:
        with open(path, 'a'):
            os.utime(path, None)
    except Error:
        pass


def remove(path):
    """ Remove a file if it exists """
    try:
        os.remove(path)
    except Error:
        pass

