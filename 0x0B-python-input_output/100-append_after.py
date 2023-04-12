#!/usr/bin/python3
""" module that contains the append_after function """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after line containing a string """
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line)
        if search_string in line:
            lines.append(new_string)
        f.seek(0)
        for line in lines:
            f.write(line)
