#!/usr/bin/python3
""" module 2-is_same_class contains the function is_same_class """


def is_same_class(obj, a_class):
    """ function that returns True if the object is an instance of a_class """
    return type(obj) == a_class
