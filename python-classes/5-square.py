#!/usr/bin/python3
"""
Defining class Square:
private attribute size, getter and setter, public method
"""


class Square:
    """Define a private instance size."""

    def __init__(self, size=0):
        """
        Initialization method with an optional size argument.
        """
        self.size = size  # This will use the setter method

    @property
    def size(self):
        """
        Getter for size attribute.
        Returns the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
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
        Returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the # character.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
