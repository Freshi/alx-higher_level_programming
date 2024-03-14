#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argc = len(sys.argv) - 1
    if argc == 1:
        print("{} argument:".format(argc))
    elif argc > 1:
        print("{} arguments:".format(argc))
    else:
        print("0 arguments.")
    for arg in range(1, len(sys.argv)):
        print("{}: {}".format(arg, sys.argv[arg]))
