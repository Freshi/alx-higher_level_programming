#!/usr/bin/python3
"""
Square class contaiing a single size attribute.
"""


class Square:
    '''Initilises a square of length size

    Attributes:
        size (int): side of one side of the square

    '''
    def __init__(self, size):
        '''
        prototype to initialise instance variables

        Attributes: size(int): size of one side
        '''
        self.__size = size
