#!/usr/bin/python3
"""
Square class that contains a private size attribute
that has a setter and a getter to retrieve it, done in
the most elegant and pythonic way
Also, has an additional method that now actually prints out
the square to stdio. Awesome!
"""


class Square:
    """
    Initialises a square of size s

    Attributes: s(int) - side of square
    """

    def __init__(self, size=0):
        """Initialises instance varaibles if provided or with defaults

        Args:

            size(int): Side of square, default: 0, optional

        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print('{}'.format("#" * self.size))
