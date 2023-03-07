#!/usr/bin/python3
i = 0
for i in range(0, 100):
    if i == 99:
        print("{:d}" .format(i))
        break
    print("{:02d}" .format(i), end=", ")
