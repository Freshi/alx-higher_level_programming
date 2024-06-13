#!/usr/bin/python3
"""
A function that adds two integers together.
"""


def add_integer(a, b=98):
    '''
    Function that adds two numbers together.
    Args:
        a (int, float) - first number
        b (int, float) - second number, default=98
    '''
    if not any((isinstance(a, int), isinstance(a, float))):
        raise TypeError('a must be an integer')
    elif not any((isinstance(b, int), isinstance(b, float))):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
