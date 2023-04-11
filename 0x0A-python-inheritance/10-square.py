#!/usr/bin/python3
""" module contains class Square that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines the class Square """

    def __init__(self, size):
        """ initializes empty square and validates the value size """
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)
