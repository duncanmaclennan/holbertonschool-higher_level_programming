#!/usr/bin/python3
"""Define an recangle module"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0  # Define the class attribute

    def __init__(self, width=0, height=0):
        """constructor function"""

        self.width = width
        self.height = height
        self.increament_number_of_instance()

    @classmethod
    def increament_number_of_instance(cls):
        """function increase no. of instance"""
        cls.number_of_instances += 1

    @classmethod
    def decrease_number_of_instance(cls):
        """function decrease no. of instance"""
        cls.number_of_instances -= 1

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

    def __str__(self):
        """defind a function that prints the rectangle"""
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        result = "#" * self.width + "\n"
        return (self.__height - 1) * result + "#" * self.width

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        self.decrease_number_of_instance()
