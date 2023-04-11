#!/usr/bin/python3
""" module 1-my_list which contains the class MyList """


class MyList(list):
    """ MyList class """

    def __init__(self):
        """ initializes the class """
        pass
    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
