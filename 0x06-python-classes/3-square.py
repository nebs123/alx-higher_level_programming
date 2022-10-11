#!/usr/bin/python3
"""This module contains the class Square"""


class Square:
    """Class Square

    This class contains the attribute size
    """

    def __init__(self, size=0):
        """This method intiializes the class Square and assignns size
        to a private field along with some constraints"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the area for the given Square object"""

        return self.__size * self.__size
