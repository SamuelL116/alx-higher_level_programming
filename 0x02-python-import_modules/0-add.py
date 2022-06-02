#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2
    from add_0 import add
    print("{0:d} + {0:d} = {0:d}".format(a, b, add(a, b)))
