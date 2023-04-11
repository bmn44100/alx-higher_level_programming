#!/usr/bin/python3
""" module contains the function add_attribute """


def add_attribute(obj, name, value):
    """ adds a new attribute to an object """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
