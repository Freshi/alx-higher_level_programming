#!/usr/bin/python3
"""
Checks if an object is an instance of a given
class or instance of class that inherits from it.
"""


def is_kind_of_class(obj, a_class):
    '''
    Checks if an object directly or indirectly inherits
    from the given class.
    Args:
        obj (any): object to check
        a_class (class) - type to check against
    Returns:
        Boolean: True or False following the check
    '''
    return isinstance(obj, a_class)
