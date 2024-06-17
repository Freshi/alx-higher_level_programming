#!/usr/bin/python3
'''
A function that returns the list
of available methods of an object.
'''


def lookup(obj):
    ''' list object attributes
         Args: obj
    '''
    return dir(obj)
