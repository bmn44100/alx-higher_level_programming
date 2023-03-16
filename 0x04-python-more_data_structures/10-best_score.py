#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = 0
        name = ''
        for key, value in a_dictionary.items():
            if a_dictionary[key] > best_score:
                name = key
                best_score = a_dictionary[key]
        return name
    return None
