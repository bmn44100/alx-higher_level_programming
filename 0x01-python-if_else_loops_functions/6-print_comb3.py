#!/usr/bin/python3
for number in range(0, 100):
    first = number // 10
    second = number % 10
    if first < second:
        if (first == 8 and second == 9):
            print("89", end="\n")
        else:
            print("{:d}" .format(first), end="")
            print("{:d}" .format(second), end=", ")
