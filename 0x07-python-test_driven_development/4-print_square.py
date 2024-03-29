#!/usr/bin/python3
"""
contains function that prints a square with the character #
"""


def print_square(size):
    """
    prints a square with the character #
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
        return
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)
