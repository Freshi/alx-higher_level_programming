#!/usr/bin/python3
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
        self.__size = size

    def __setattr__(self, name, value):
        if name == 'size':
            if type(value) != int:
                raise TypeError('size must be integer')
            elif value < 0:
                raise ValueError('size must be >= 0')
        self.__dict__[f"__(name)"] = value
