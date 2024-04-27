#!/usr/bin/python3
"""
Square class that contains a private size attribute
that is set using the __setattri__ setter method
"""


class Square:
    """
    Initialises a square of size s

    Attributes: s(int) - side of square
    """

    def __init__(self, size=0):
        """Initialises instance varaibles if provided or with defaults

        Args:

            size(int): Side of square, default: 0

        """
        self.set_size(size)

    def set_size(self, new_size):
        if type(new_size) is not int:
            raise TypeError('size must be an integer')
        elif new_size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = new_size
