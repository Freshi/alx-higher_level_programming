#!/usr/bin/python3
for i in range(ord('z'), ord('z') - 26, -2):
    print("{}{}".format(chr(i), chr((i-1) - 32)), end='')
