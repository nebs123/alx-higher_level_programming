#!/usr/bin/python3
"""This is a module to hold the Rectangle class"""


class Rectangle:
    """An Rectangle class with width and height property
       Can also calculate the area and perimeter
       Can produce str and repr strings
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area for the rectangle"""

        return self.width * self.height

    def perimeter(self):
        """calculates the perimeter for the rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """Returns a human readable string representation
        of a rectangle using #"""

        ret = ""
        if self.width == 0 or self.height == 0:
            return ret

        for i in range(self.height):
            for j in range(self.width):
                ret += str(self.print_symbol)
            if i < self.height - 1:
                ret += "\n"
        return ret

    def __repr__(self):
        """Returns an evaluatable reprsentation of the class"""

        return "Rectangle(" + str(self.width) + ", " +\
            str(self.height) + ")"

    def __del__(self):
        """Code that runs when object is deleted"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
