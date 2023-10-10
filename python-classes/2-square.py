#!/usr/bin/python3
"""
Module for defining a Square with conditions.
"""


class Square:
    """
    Class that defines a square with a private instance attribute size.
    Includes input validation.
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
