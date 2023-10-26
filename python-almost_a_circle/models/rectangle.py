#!/usr/bin/python3
"""Define Sub Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Subclass class init"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiate instance var"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # access Base class def

    @property
    def width(self):
        """get width"""

        return self.__width

    @width.setter
    def width(self, value):
        """set width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x"""

        return self.__x

    @x.setter
    def x(self, value):
        """set x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y"""

        return self.__y

    @y.setter
    def y(self, value):
        """set y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Define a function that caculate area of rectangle area"""
        return self.__width * self.__height

    def display(self):
        """define a function that print a rectangle"""
        print("\n" * self.y, end="")
        for r in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        # self.id has been initialised in def__init__
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assign arguments"""
        # only reach **kwargs when *args is empty
        if len(args) == 0:
            for k, v in kwargs.items():
                self.__setattr__(k, v)
            return

        try:
            # calling def setter, or can also put self.__width
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """return dictionary"""

        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
