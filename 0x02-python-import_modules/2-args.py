#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    i = 1
    if args == 1:
        print("0 arguments.")
    else:
        if args == 2:
            print("{:d}" .format(args - 1), "argument:")
        elif args > 2:
            print("{:d}" .format(args - 1), "arguments:")
        while args != 1:
            print("{:d}:" .format(i), sys.argv[i])
            i += 1
            args -= 1
