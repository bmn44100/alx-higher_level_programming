#!/usr/bin/python3
""" module 8-rectangle contains the subclass Rectangle
which inherits from the class BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines the class Rectangle """
    def __init__(self, width, height):
        """ initializes class Rectangle """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
