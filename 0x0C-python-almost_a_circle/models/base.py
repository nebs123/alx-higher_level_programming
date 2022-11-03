#!/usr/bin/python3
"""Contains base class Base which others extend"""


class Base:
    """Base class which handles id of created objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer for base class; assigns id to object"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
