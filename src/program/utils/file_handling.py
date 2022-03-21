import os


def touch(path):
    try:
        with open(path, 'a'):
            os.utime(path, None)
    except Error as error:
        print(error)


def remove(path):
    try:
        os.remove(path)
    except Error as error:
        print(error)

