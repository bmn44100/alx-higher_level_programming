#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    new_list = list(my_set)
    sum = 0
    for i in range(0, len(new_list)):
        sum += new_list[i]
    return sum
