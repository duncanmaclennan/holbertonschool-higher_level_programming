#!/usr/bin/python3
"""Define Sub Class square"""
from models.rectangle import Rectangle


class Square(Rectangle):  # inherite all attribute/var from Rectangle
    """Subclass class init"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiate instance var"""

        # can also use key:value format "width=size"
        super().__init__(size, size, x, y, id)

    def __str__(self):  # each class has its own __str__
        """print str"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}"

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        # cannot put self.__width due to private, so call etter function
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assign arguments"""
        # only reach **kwargs when *args is empty
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            # calling def setter, or can also put self.__width
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """return dictionary"""

        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
