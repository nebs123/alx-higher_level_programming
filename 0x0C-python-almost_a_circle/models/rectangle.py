#!/usr/bin/python3
"""Holds the code for the Rectangle class"""


from .base import Base


class Rectangle(Base):
    """Code for the Rectangle class that models a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class by calling super class and also assigns the
        remaining attributes to their respective properties"""

        super().__init__(id)

        self.width = width
        self.height = height

        self.x = x
        self.y = y

    @property
    def width(self):
        """property getter for self.__width"""

        return self.__width

    @width.setter
    def width(self, value):
        """property setter for self.__width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """property getter for self.__height"""

        return self.__height

    @height.setter
    def height(self, value):
        """property setter for self.__height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """property getter for self.__x"""

        return self.__x

    @x.setter
    def x(self, value):
        """property setter for self.__x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """property getter for self.__y"""

        return self.__y

    @y.setter
    def y(self, value):
        """property setter for self.__y"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Calculate area for the Rectangle"""

        return self.width * self.height

    def display(self):
        """Prints out rectangle using the #"""

        for i in range(self.y):
            print()

        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"
