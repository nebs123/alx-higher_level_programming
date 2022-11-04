#!/usr/bin/python3
"""Test case for base.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBase(unittest.TestCase):
    """Class to test constructor of Base.py"""

    def test_base(self):
        """Test creation of Base objects"""
        obj1 = Base()
        obj2 = Base()
        obj3 = Base(12)
        obj4 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 12)
        self.assertEqual(obj4.id, 3)

    def test_to_json_str(self):
        """Tests the static method to_json_string of Base class"""

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{}]), "[{}]")
        d1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(Base.to_json_string([d1]),
                         '[{"x": 2, "width": 10, "id": 1, \
"height": 7, "y": 8}]')

        d2 = {"x": 4, "width": 8, "id": 5, "height": 2, "y": 1}
        self.assertEqual(Base.to_json_string([d1, d2]),
                         '[{"x": 2, "width": 10, "id": 1, \
"height": 7, "y": 8}, {"x": 4, "width": 8, "id": 5, "height": 2, "y": 1}]')

    def test_save_to_file(self):

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

        l1 = [Rectangle(4, 2, 5, 4, 20), Rectangle(5, 5, 3, 1, 21)]
        Rectangle.save_to_file(l1)

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(json.loads(f.read()), [l1[0].to_dictionary(),
                                                    l1[1].to_dictionary()])

        l1 = [Square(10, 1, 2, 12), Square(5, 2, 1, 8)]
        Square.save_to_file(l1)

        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual(json.loads(f.read()), [l1[0].to_dictionary(),
                                                    l1[1].to_dictionary()])

    def test_from_json_string(self):
        """tests the static method from_json_string"""

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        l1 = [{"id": 12, "width": 5, "height": 12}, {"size": 12, "x": 3, "y": 4}]
        self.assertEqual(l1, Base.from_json_string(Base.to_json_string(l1)))

        l1 = [{}, {}]
        self.assertEqual(l1, Base.from_json_string(Base.to_json_string(l1)))

    def test_create(self):
        """tests the create method of the Base class"""

        r1 = Rectangle(1, 5)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))

        s1 = Square(10, 1, 2, 3)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 == s2)

    def test_load_from_file(self):
        """tests the loading from file capability of Base.load_from_file"""

        self.assertEqual(Base.load_from_file(), [])

        l1 = [Rectangle(4, 2, 5, 4, 20), Rectangle(5, 5, 3, 1, 21)]
        Rectangle.save_to_file(l1)

        l2 = Rectangle.load_from_file()

        self.assertFalse(l1 == l2)

        for i in range(len(l1)):
            with self.subTest(i=i):
                self.assertEqual(str(l1[i]), str(l2[i]))

        l1 = [Square(10, 1, 2, 12), Square(5, 2, 1, 8)]
        Square.save_to_file(l1)

        l2 = Square.load_from_file()

        self.assertFalse(l1 == l2)
        for i in range(len(l1)):
            with self.subTest(i=i):
                self.assertEqual(str(l1[i]), str(l2[i]))
