import unittest

from io import StringIO
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare (unittest.TestCase):
    """
    Test cases for Square
    """

    def test_valid_input(self):
        """
        Test for input/arg
        """
        s0 = Square(1)
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s0.size, 1)
        self.assertEqual(s0.x, 0)
        self.assertEqual(s0.y, 0)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 4)

    def test_invalid_input(self):
        """
        Test for str args
        """
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, 1.1, 1.2)
        self.assertRaises(ValueError, Square, -1, 1)

    def test_area(self):
        """
        Test area of Square
        """
        r = Square(2)
        self.assertEqual(r.area(), 4)

    def test_display_no_x_and_y_offset(self):
        """
        Tests that the graphical representation prints out correctly
        """
        r = Square(2, 2)
        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        r.display()                     # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "  ##\n  ##\n")

    def test_str(self):
        """
        Test __str__()
        """
        r = Square(1, 2, 3, 4)
        self.assertEqual(str(r), "[Square] (4) 2/3 - 1")

    def test_update(self):
        """
        Test if attributes update
        """
        r = Square(1, 2, 3, 4)
        r.update(5)
        self.assertEqual(r.id, 5)

    def test_to_dictionary(self):
        """
        Test return dict representation of a Rect
        """
        r = Square(1, 2, 3, 4)
        r_dict = r.to_dictionary()
        output = {'size': 1, 'x': 2, 'y': 3, 'id': 4}
        self.assertEqual(r.to_dictionary(), output)


if __name__ == "__main__":
    unittest.main()
