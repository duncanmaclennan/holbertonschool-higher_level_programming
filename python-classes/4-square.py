#!/usr/bin/python3
"""
Module for defining a Square with conditions, area calculation, and property setters/getters.
"""


class Square:
    """
    Creating Squares

    Attributes:
        __size: (int): Size of square

    Methods:
        __init__(self, size=0): initiliases square with default 0
        area(self): calculates current square area


    """

    def __init__(self, size=0):
        """
        Initialises new Square instance

        Args:
            size (int): size of the square
        """
        self.size = size  # This will use the setter method

    @property
    def size(self):
        """
        Function to get value of __size

        Getter for size attribute.
        Returns the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Function to set value of __size

        Setter for size attribute with type and value validation.
        """
        # Type verification
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Value verification
        if value < 0:
            raise ValueError("size must be >= 0")

        # Assigning the value
        self.__size = value

    def area(self):
        """
        Function that calculates the current square area

        Returns the current square area.
        """
        return self.__size ** 2
