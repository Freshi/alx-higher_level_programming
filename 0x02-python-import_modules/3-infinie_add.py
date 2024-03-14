#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum = 0
    for _ in sys.argv[1:]:
        sum += int(_)
    print("{}".format(sum))
