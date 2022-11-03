#!/usr/bin/python3
"""Test case for base.py"""


import unittest
from models.base import Base


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
