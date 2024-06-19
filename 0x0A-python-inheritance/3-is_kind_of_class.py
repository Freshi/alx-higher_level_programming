#!/usr/bin/python3
'''
Checks if an object is an instance of
class or instance of class that inherits
from given class
'''


def is_kind_of_class(obj, a_class):
    '''
    Compares obj to class
        Args:
            obj (obj) - object to check
            a_class (class) - type to compare to
    '''
    return isinstance(obj, a_class)
