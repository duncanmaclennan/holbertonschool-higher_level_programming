#!/usr/bin/python3
"""
Defining a Rectangle
"""


class Rectangle:
    """
    Adding width and height
    """

    def __init__(self, width=0, height=0):
        """
        Args:
            width: int
            height: int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Function to get value of width

        Return:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Function to set value of width

        Arg:
            value: int

        Raises:
            TypeError: width must be an int
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Function to get value of height

        Return:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Function to set value of height

        Arg:
            value: int
        Raises:
            TypeError: height must be an int
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
