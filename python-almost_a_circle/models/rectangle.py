#!/usr/bin/python3
"""
Inheriting from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherits from class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Function initialises new Rectangle instance

        Args:
            width: int
            height: int
            x: int
            y: int
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        prints Rectangle instance with #
        """
        for line in range(self.y):
            print("")
        for i in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        Return [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.__x, self.__y, self.__width,
            self.__height)

    def update(self, *args, **kwargs):
        """
        Update attribute values
        """
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass

        else:
            try:
                self.id = kwargs["id"]
            except KeyError:
                pass
            try:
                self.width = kwargs["width"]
            except KeyError:
                pass
            try:
                self.height = kwargs["height"]
            except KeyError:
                pass
            try:
                self.x = kwargs["x"]
            except KeyError:
                pass
            try:
                self.y = kwargs["y"]
            except KeyError:
                pass

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
