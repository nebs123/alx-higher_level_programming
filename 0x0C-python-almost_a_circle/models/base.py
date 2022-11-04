#!/usr/bin/python3
"""Contains base class Base which others extend"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json string representation of list of dictionaries"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of Base descendant instances into file"""
        dict_list = []

        if list_objs is not None:
            for elem in list_objs:
                dict_list.append(elem.to_dictionary())

        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """retrieves list object from json string"""

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create class based on dictionary values"""

        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Load instances of cls object from file"""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                dict_list = Base.from_json_string(f.read())
        except FileNotFoundError:
            return []
        obj_list = []

        for elem in dict_list:
            obj_list.append(cls.create(**elem))

        return obj_list
