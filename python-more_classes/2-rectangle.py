#!/usr/bin/python3
"""Define an recangle module"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """constructor function"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """define a function that calculate the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """defind a function that calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width + self.__height) * 2
