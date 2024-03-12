#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 65:
	    print("{}".format(chr(ord(c) - 32)), end='')
        else:
	    print(chr(ord(c)), end="")
