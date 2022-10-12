#!/usr/bin/python3
"""Module that holds MagicClass which is constructed from bytecode"""


class MagicClass:
    """Class that is constructed based on bytecode"""

    def __init__(self, radius=0):
        """Initalizer for the MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the area of a Circle I think?!?!?!?"""
        import math
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of a Circle I think"""
        import math
        return 2 * math.pi * self.__radius
