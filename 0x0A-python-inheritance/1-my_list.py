#!/usr/bin/python3
'''
MyList class that inherits from a list
'''


class MyList(list):
    ''' MyList class definition
    which inherits from list and has
    all its methods
    '''
    def print_sorted(self):
        # prints itself sorted in ascending order
        print(sorted(self))
        return sorted(self)
