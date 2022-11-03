#!/usr/bin/python3
"""Module that holds the class Square"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Class that represents a Square object"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the class along with super class constructors"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation of Square"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter property for the size of the square"""

        return self.width

    @size.setter
    def size(self, value):
        """setter property for the size of the square"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the attributes of the rectangle"""

        if len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            else:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
