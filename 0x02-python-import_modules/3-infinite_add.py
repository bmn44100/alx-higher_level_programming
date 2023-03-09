#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    i = 1
    sum_of_args = 0
    if args == 1:
        print("0")
    else:
        if args == 2:
            print(sys.argv[i])
        else:
            while args != 1:
                sum_of_args += int(sys.argv[i])
                i += 1
                args -= 1
            print("{:d}" .format(sum_of_args)
