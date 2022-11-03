#!/usr/bin/python3
"""contains test case for the square class"""


from models.square import Square
import sys
from io import StringIO
import unittest


class TestSquare(unittest.TestCase):
    """Tests for the Square class"""

    def test_values(self):
        """tests whether the values are passed correctly in constructor"""
        s1 = Square(5, id=1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2, id=2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)

    def test_square_type_errors(self):
        """Test the value and type errors"""

        with self.assertRaises(TypeError, msg="height must be an integer"):
            r = Square(10)
            r.height = "Whats up"

        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square(10.2)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r = Square(10)
            r.width = 1.15

        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(10, {}, 4)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r = Square(10, 2)
            r.x = {}

        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(10, 4, "5")
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Square(10, 2)
            r.y = "Hello"

    def test_square_value_errors(self):
        """Test value errors"""

        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(-3, 5)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r = Square(10, 5)
            r.width = 0
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r = Square(10, 5)
            r.width = -120
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(0, 5)

        with self.assertRaises(ValueError, msg="height must be > 0"):
            r = Square(10, 2)
            r.height = -120
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r = Square(10, 2)
            r.height = 0

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Square(10, -5, 7)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r = Square(10, 2)
            r.x = -1

        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Square(10, 7, -5)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r = Square(10, 2)
            r.y = -1

    def test_square_display(self):
        """tries to test the display method of class rectangle"""
        temp = sys.stdout
        string = StringIO()
        sys.stdout = string
        rect = Square(4)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(),
                         "####\n####\n####\n####\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Square(3)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "###\n###\n###\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Square(2)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "##\n##\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Square(1)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "#\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Square(2, 2, 1)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "\n  ##\n  ##\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Square(1, 3, 0)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "   #\n")
        string.close()

        string = StringIO()
        sys.stdout = string
        rect = Square(3, 0, 3)
        rect.display()
        string.seek(0)
        self.assertEqual(string.getvalue(), "\n\n\n###\n###\n###\n")
        string.close()

        sys.stdout = temp

    def test_size(self):
        """tests the functionality of the size property"""

        s1 = Square(5, id=1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError, msg="width must be an integer"):
            s1.size = 10.2
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s1.size = "10"
        with self.assertRaises(ValueError, msg="width must be > 0"):
            s1.size = 0
        with self.assertRaises(ValueError, msg="width must be > 0"):
            s1.size = -25

    def test_square_update(self):

        s1 = Square(5, id=1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(1, id=5, size=12)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")
