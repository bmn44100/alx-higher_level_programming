#!/usr/bin/python3
""" module that contains the class Student """


class Student:
    """ defines the class Student """

    def __init__(self, first_name, last_name, age):
        """ initializes a new Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for att in attrs:
            if type(att) is not str:
                return self.__dict__
        return {x: self.__dict__[x] for x in self.__dict__ if x in attrs}
