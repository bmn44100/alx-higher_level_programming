#!/usr/bin/python3
def uppercase(str):
    for char in str:
        num_char = ord(char)
        if num_char in range(97, 123):
            num_char = num_char - 32
        char = chr(num_char)
        print("{:s}" .format(char), end="")
    print()
