#!/usr/bin/python3
'''
Function that checks for type of
object and returns a boolean.
'''


def is_same_class(obj, a_class):
    '''
    Checks if object is of type class;
        Args:
            obj (obj) - object to check
            a_class (class) - class to compare
    '''
    return type(obj) is a_class
