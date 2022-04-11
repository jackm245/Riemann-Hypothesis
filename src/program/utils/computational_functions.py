"""
computational_functions.py
==========================

Contains subroutines and classes that are used for various different algorithms

Subroutines:
    - binary_search
    - binary_insertion_sort
    - save_zeta_zeroes_to_file
    - save_zeta_values_to_file
    - save_zeta_to_file
    - change_datatype

Classes
    - Queue
    - Stack
"""


import random
import time
import csv
import re
import os


def binary_search(data, target):

    """
    For a set of unique elements that are sorted in ascending order (data),
    this function will return the index where target is in the data, with time
    complexity O(log n)
    """

    low = 0
    high = len(data)
    if target < min(data):
        return 0
    elif target > max(data):
        return len(data)
    else:
        while True:
            mid = (high+low) // 2
            if data[mid] < target < data[mid+1]:
                return mid+1
            elif target < data[mid]:
                high=mid
            elif target > data[mid]:
                low=mid
            else:
                raise ValueError('Error: Input list was not a set')


def binary_insertion_sort(data, descending=False):

    """
    Sorts a list of data into ascending order using a binary insertion sort
    """

    try:
        array = list(map(float, data ))
    except ValueError:
        array = data
    queue = Queue(input_queue=array)
    sorted = [queue.deQueue()]
    while not queue.is_empty():
        item = queue.deQueue()
        index = binary_search(sorted, item)
        bigger = sorted[index:]
        del sorted[index:]
        sorted.append(item)
        sorted.extend(bigger)
    if not descending:
        return sorted
    else:
        return sorted[::-1]


class Queue:

    """
    Implementation of a circular queue

    Contains the methods:
        - enQueue
        - deQueue
        - is_full
        - is_empty

    """

    def __init__(self, **kwargs):
        self.input_queue = kwargs.get('input_queue', [])
        self.size = len(self.input_queue)
        self.max_size = kwargs.get('max_size', self.size)
        self.front = 0
        self.rear = self.size
        # if doesnt work, use len(self.input_queue) instead of self.size
        if self.size > self.max_size:
            raise IndexError("max_size must be greater than or equal to the \
                    size of the input queue")
        else:
            self.blanks = [False for i in range(self.max_size - self.size)]
            self.queue = self.input_queue + self.blanks

    def enQueue(self, item):

        """
        Appends an item to the rear of the circular queue
        """

        if self.is_full():
            raise IndexError("Tried to enqueue to a full queue")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear+1) % self.max_size
            self.size += 1

    def deQueue(self):

        """
        Remove and return the value at the front of the circular queue
        """

        if self.is_empty():
            raise IndexError("Tried to dequeue from an empty queue")
        else:
            item = self.queue[self.front]
            self.queue[self.front] = False
            self.front = (self.front+1) % self.max_size
            self.size -= 1
            return item

    def is_full(self):

        """
        Check if the circular queue is full
        """

        return self.size == self.max_size

    def is_empty(self):

        """
        Check if the circular queue is empty
        """

        return self.size == 0

    def get_size(self):

        """
        Returns the number of elements in the queue
        """

        return self.size

    def get_queue(self):

        """
        Returns the queue as a list
        """

        return self.queue

    def __str__(self):

        """
        Return a printable value of the queue
        """

        return 'Queue(' + ', '.join([str(i) for i in self.queue]) + ')'


class Stack:

    """
    Implementation of a stack

    Contains the methods:
        - push
        - pop
        - is_full
        - is_empty
        - peek
        - size

    """
    class UnderflowError(Exception):

        """
        Create an UnderflowError exception, as this does not exist by default in python
        """

        def __init__(self, error_message):
            self.error_message = error_message

        def __str__(self):
            return self.error_message

    def __init__(self, **kwargs):
        self.stack = kwargs.get('input_list', [])
        self.size = len(self.stack)
        self.max_size = kwargs.get('max_size', 1024)
        if self.size > self.max_size:
            raise IndexError("max_size must be greater than or equal to the \
                    size of the input queue")


    def push(self, item):

        """
        Add an item to the stack
        """
        if self.size < max_size:
            self.stack.append(item)
            self.stack.size += 1
        else:
            raise OverflowError("Unable to push to a full stack")

    def pop(self):

        """
        Remove the item at the top of the stack
        """
        try:
            item = self.stack[-1]
        except IndexError:
            raise UnderflowError("Unable to pop from an empty stack")
        del self.stack[-1]
        self.stack.size -= 1
        return item

    def is_full(self):

        """
        Check if the stack is full
        """

        return self.size == self.max_size

    def is_empty(self):

        """
        Check if the stack is empty
        """

        return self.get_size() == 0

    def peek(self):

        """
        Return the top item without removing it
        """

        return self.stack[-1]

    def get_size(self):

        """
        Returns the number of elements in the stack
        """

        return self.size

    def __str__(self):

        """
        Return a printable value of the queue
        """

        return 'Stack(' + ', '.join([str(i) for i in self.stack]) + ')'


def save_zeta_values_to_file(table_values, filepath,
        fieldnames=['InputReal', 'InputImag', 'OutputReal', 'OutputImag']):

    """
    Given a list of corresponding inputs and outputs of the zeta function,
    save these sets of values to a file.
    """

    csv_values = [list(map(str,
        [input.get_real(), input.get_imag(), output.get_real(), output.get_imag()]))
        for input, output in table_values]
    regex = r'-?\d+\.\d+'
    index = 0
    save_zeta_to_file(csv_values, filepath, regex, index, fieldnames)


def save_zeta_zeroes_to_file(table_values, filepath,
        fieldnames=['InputReal', 'InputImag', 'OutputReal', 'OutputImag']):

    """
    Given a list of zeroes/roots of the zeta function,
    save these zeroes to a file
    """

    csv_values = [list(map(str, [real, imag])) for real, imag in table_values]
    regex = r'-?\d+\.\d+'
    index = 1
    save_zeta_to_file(csv_values, filepath, regex, index, fieldnames)


def save_zeta_to_file(csv_values, filepath, regex, index, fieldnames):

    """
    Given a list of complex numbers, combine these with the contents of the
    file that they are going to be saved to, sort these values using the first
    real number, and save them back into the csv file
    """

    if not os.path.isfile(filepath):
        os.mknod(filepath)
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row != fieldnames:
                csv_values.append(list(map(str, row)))
    sorting_dict = {float(str(list(map(float,
        re.findall(regex, ','.join(row))))[index]) + str(row_no)) : row for row_no, row in enumerate(csv_values)}
    sorted_keys = binary_insertion_sort(list(set(sorting_dict.keys())))
    sorted_values = [sorting_dict[key] for key in sorted_keys]
    with open(filepath, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fieldnames)
        for row in sorted_values:
            csv_writer.writerow(row)


def change_datatype(value, datatype):

    """
    Change the datatype of a value, if the datatype is given as a string, and not
    as a python keyword
    """

    match str(datatype):
        case 'int':
            return int(value)
        case 'str':
            return str(value)
        case 'float':
            return float(value)
        case 'bool':
            return bool(value)
        case 'list':
            return list(value)
        case 'complex':
            return Complex(value)
        case 'fraction':
            return Fraction(value)
        case _:
            raise TypeError(f'Trying to change vlaue \'{value}\' \
                    to invalid datatype \'{datatype}\'')
