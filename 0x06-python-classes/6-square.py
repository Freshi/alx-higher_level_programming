#!/usr/bin/python3
"""
Square class with two private instance attributes
one for size and another for position
both having a getter and setter. It also has 2 public methods
for getting the area and printing out the square at position.
"""


class Square:
    """
    Initialises a square of size s

    Attributes: s(int) - side of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialises instance varaibles if provided or with defaults

        Args:

            size(int): Side of square, default: 0, optional
            position(tuple): Position where the square is printed,
            default: (0,0), optional

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        if type(position) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        elif self.position[1]:
            print('\n' * (self.position[1]-1))
            for i in range(self.size):
                print('{}{}'.format(" " * self.position[0], "#" * self.size))
        else:
            for i in range(self.size):
                print('{}{}'.format(" " * self.position[0], "#" * self.size))
