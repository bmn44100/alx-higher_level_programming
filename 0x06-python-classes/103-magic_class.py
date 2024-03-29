#!/usr/bin/python3
"""Python class MagicClass for implementing bytecode"""


import math


class MagicClass:
    """defines a circle"""

    def __init__(self, radius=0):
        """initializes the circle"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """returns area of a circle"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """returns circumference of a circle"""
        return 2 * math.pi * self.__radius
