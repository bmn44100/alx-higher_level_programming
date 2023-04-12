#!/usr/bin/python3
""" module that contains pascal_triangle function """


def pascal_triangle(n):
    """ returns a list of lists of integers representing Pascal’s triangle """
    if n <= 0:
        return []
    p_t = [[] for x in range(n)]
    p_t[0] = [1]
    if n > 1:
        p_t[1] = [1, 1]
    if n > 2:
        for i in range(2, n):
            p_t[i].append(1)
            for j in range(i - 1):
                p_t[i].append(p_t[i - 1][j] + p_t[i - 1][j + 1])
            p_t[i].append(1)
    return p_t
