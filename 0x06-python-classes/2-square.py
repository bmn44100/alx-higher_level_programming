#!/usr/bin/python3
class Square:
    """module that defines a square"""
    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
            return
        if (size < 0):
            raise ValueError("size must be >= 0")
            return
