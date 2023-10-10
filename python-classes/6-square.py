#!/usr/bin/python3
"""
Module for defining a Square with conditions, area calculation, property setters/getters, position attribute, and a print method.
"""


class Square:
    """
    Class that defines a square with private attributes size and position.
    Includes input validation, a method to compute the area, property setters/getters, and a method to print the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization method with an optional size and position arguments.
        """
        self.size = size  # This will use the size setter
        self.position = position  # This will use the position setter

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter for position attribute.
        Returns the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position attribute with type and value validation.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not isinstance(value[0], int) or not isinstance(value[1], int) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the # character considering the position attribute.
        """
        if self.__size == 0:
            print()
            return

        # Print the top padding (vertical position)
        print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            # Print the left padding (horizontal position)
            print(" " * self.__position[0], end="")
            # Print the square
            print("#" * self.__size)
