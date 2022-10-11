#!/usr/bin/python3
"""This module contains the class Square"""


class Square:
    """Class Square

    This class contains the attribute size
    """

    def __init__(self, size=0, position=(0,0)):
        """This method intiializes the class Square and assignns size
        to a private field along with some constraints"""

        self.size = size
        self.position = position

    def area(self):
        """Calculates and returns the area for the given Square object"""

        return self.__size * self.__size

    @property
    def size(self):
        """size property that returns the value of self.__size"""

        return self.__size

    @size.setter
    def size(self, size):
        """setter property for self.__size"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """getter for the attribute __position"""

        return self.__position

    @position.setter
    def position(self, position):
        """setter property for the attribute __position"""

        if type(position) != tuple or len(position) != 2 \
           or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """This method prints the square using hashtags # and adding
        spaces to offset for the position"""

        if (self.size == 0):
            print()
            return

        for i in range(self.position[1]):
            print()

        for i in range(self.size):
            for j in range(self.size + self.position[0]):
                if j < self.position[0]:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()
