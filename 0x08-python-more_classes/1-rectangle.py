#!/usr/bin/python3
'''
Rectangle
    -Initialises a class rectangle with a width and height.
'''

class Rectangle:
    '''
    Initialises a rectangle object
        width - int, width of rectangle, not negtive
        height - int, height of rectangle, not negative
    '''

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an interger')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an interger')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

