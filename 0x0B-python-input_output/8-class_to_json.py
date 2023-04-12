#!/usr/bin/python3
""" module that contains the class_to_json function """


def class_to_json(obj):
    """ returns dictionary description for JSON serialization of an object """
    return obj.__dict__
