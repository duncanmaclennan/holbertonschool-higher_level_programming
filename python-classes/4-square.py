#!/usr/bin/python3
"""
Defining class Square - private attribute size
getter and setter, public method
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
        self.size = size

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

        Args:
            value (int): size of square

        Raises:
            TypeError: value must be an int
            ValueError: value must be greater than 0
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
