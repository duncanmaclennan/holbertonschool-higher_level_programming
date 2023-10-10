#!/usr/bin/python3
"""
Module for defining a Square with conditions and area calculation.
"""


class Square:
    """
    Class that defines a square with a private instance attribute size.
    Includes input validation and a method to compute the area.
    """

    def __init__(self, size=0):
        """
        Initialization method with an optional size argument.
        """
        # Type verification
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Value verification
        if size < 0:
            raise ValueError("size must be >= 0")

        # Assigning the value
        self.__size = size

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2
