#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real = 0
    for i in my_list:
        try:
            if (i <= x):
                print("{:d}" .format(i), end="")
                real += 1
        except IndexError:
            return None
    print(end="\n")
    return (real)
