#!/usr/bin/python3
"""  module 3-is_kind_of_class contains the function is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of, or if the
    is an instance of a class that inherited from, the specified class """
    return isinstance(obj, a_class)
