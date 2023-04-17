#!/usr/bin/python3
""" module that contains the class Base """


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor that initializes the class base """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
