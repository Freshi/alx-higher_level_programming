#!/usr/bin/python3
'''
Checks if an object is a subclass of a given
class
'''


def inherits_from(obj, a_class):
    '''
    Check if obj is subclass of a_class
    '''
    return issubclass(obj.__class__, a_class) and (type(obj) is not a_class)
