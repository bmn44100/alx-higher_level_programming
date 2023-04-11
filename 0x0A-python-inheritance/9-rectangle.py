#!/usr/bin/python3
""" module 8-rectangle contains the subclass Rectangle
which inherits from the class BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines the class Rectangle """
    def __init__(self, width, height):
        """ initializes class Rectangle """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns area of a Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ returns string representation of Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
