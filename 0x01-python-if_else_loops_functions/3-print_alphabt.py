#!/usr/bin/python3
i = 0
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    print("{:s}" .format(chr(i)), end="")
