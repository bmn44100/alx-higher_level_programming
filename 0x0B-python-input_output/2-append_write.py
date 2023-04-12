#!/usr/bin/python3
""" module that contains the append_write function """


def append_write(filename="", text=""):
    """ appends a string to a text file (UTF8) """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
