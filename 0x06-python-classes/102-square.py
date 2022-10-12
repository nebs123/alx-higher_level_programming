#!/usr/bin/python3
"""This module contains the class Square"""


class Square:
    """Class Square

    This class contains the attribute size
    """

    def __init__(self, size=0):
        """This method intiializes the class Square and assignns size
        to a private field along with some constraints"""

        self.size = size

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

    def __eq__(self, other):
        """ Compares if two square are equal based on their area """

        return self.area() == other.area()

    def __ne__(self, other):
        """ Compares if two square are not equal based on their area """

        return self.area() != other.area()

    def __lt__(self, other):
        """ Checks if area of self square is less than that of other square"""

        return self.area() < other.area()

    def __le__(self, other):
        """ Checks if area of self square is less than
        or equal to  that of other square"""

        return self.area() <= other.area()

    def __gt__(self, other):
        """ Checks if area of self square is greater than that
        of other square"""

        return self.area() > other.area()

    def __ge__(self, other):
        """ Checks if area of self square is greater or
        equal than that of other square"""

        return self.area() >= other.area()
