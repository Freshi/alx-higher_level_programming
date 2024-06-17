#!/usr/bin/python3
'''
MyList class that inherits from a list
'''


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
