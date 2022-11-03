#!/usr/bin/python3
"""Contains test cases for the Rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO


class TestRect(unittest.TestCase):
    """Tests for the Rectangle class"""

    def test_init(self):
        """Tests creation of the Rectangle"""

        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Base)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10, 5, 6, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 6)

    def test_type_errors(self):
        """Test the value and type errors"""

        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r = Rectangle(10, 2)
            r.height = "Whats up"

        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle(10.2, 5)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r = Rectangle(10, 2)
            r.width = 1.15

        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(10, 2, {}, 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(10, 2, 4, "5")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Rectangle(10, 2)
            r.y = "Hello"

    def test_value_errors(self):
        """Test value errors"""

        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-3, 5)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r = Rectangle(10, 5)
            r.width = 0
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r = Rectangle(10, 5)
            r.width = -120
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 5)

        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(5, 0)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(5, -5)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r = Rectangle(10, 2)
            r.height = -120
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r = Rectangle(10, 2)
            r.height = 0

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(10, 2, -5, 7)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r = Rectangle(10, 2)
            r.x = -1

        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(10, 2, 7, -5)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r = Rectangle(10, 2)
            r.y = -1

    def test_area(self):
        """test for the area method of class rectangle"""

        self.assertEqual(Rectangle(10, 2).area(), 20)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(5, 4).area(), 20)
        self.assertEqual(Rectangle(1, 2).area(), 2)
        self.assertEqual(Rectangle(5, 6).area(), 30)

    def test_display(self):
        """tries to test the display method of class rectangle"""
        temp = sys.stdout
        string = StringIO()
        sys.stdout = string
        rect = Rectangle(4, 6)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(),
                         "####\n####\n####\n####\n####\n####\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Rectangle(2, 2)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "##\n##\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Rectangle(2, 1)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "##\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Rectangle(1, 2)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "#\n#\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Rectangle(1, 2, 2, 1)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "\n  #\n  #\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Rectangle(2, 1, 3, 0)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "   ##\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Rectangle(3, 4, 0, 3)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "\n\n\n###\n###\n###\n###\n")
        string.close()

        sys.stdout = temp

    def test_str_dunder(self):
        """tests whether the magic method __str__ works correctly"""

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1, 5, 7)
        self.assertEqual(str(r2), "[Rectangle] (7) 1/5 - 5/5")

        r3 = Rectangle(2, 1, 0, 0, 25)
        self.assertEqual(str(r3), "[Rectangle] (25) 0/0 - 2/1")

    def test_update(self):
        """tests whether the method update works properly"""

        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update2(self):
        """tests the revised version of update"""

        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(10, id=15, width=1)
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/10")

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (10) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")
