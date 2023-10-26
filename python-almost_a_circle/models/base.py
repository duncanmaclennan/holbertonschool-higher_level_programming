#!/usr/bin/python3
"""
Inheriting from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Function initialises new Rectangle instance

        Args:
            size: int
            x: int
            y: int
        """
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        """
        Return string format
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attributes
        """
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

        else:
            try:
                self.id = kwargs["id"]
            except KeyError:
                pass
            try:
                self.size = kwargs["size"]
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
        Returns the dictionary representation of a Square
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
