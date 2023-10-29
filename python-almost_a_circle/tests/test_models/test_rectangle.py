import unittest

from io import StringIO
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle (unittest.TestCase):
    """
    Test cases for Rectangle
    """

    def test_valid_input(self):
        """
        Test for input/arg
        """
        r0 = Rectangle(1, 2)
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 0)
        self.assertEqual(r0.y, 0)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def test_invalid_input(self):
        """
        Test for str args
        """
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(TypeError):
            Rectangle(None)
        with self.assertRaises(TypeError):
            Rectangle(1.1, 1.2)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """
        Test area of Rectangle
        """
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)

    def test_display_no_x_and_y_offset(self):
        """
        Tests that the graphical representation prints out correctly
        """
        r = Rectangle(2, 2)
        capturedOutput = StringIO()     # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        r.display()                     # Call unchanged function.
        sys.stdout = sys.__stdout__     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), "##\n##\n")

    def test_str(self):
        """
        Test __str__()
        """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update(self):
        """
        Test if attributes update
        """
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6)
        self.assertEqual(r.id, 6)

    def test_to_dictionary(self):
        """
        Test return dict representation of a Rect
        """
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        output = {'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5}
        self.assertEqual(r.to_dictionary(), output)

    def test_load_from_file(self):
        """
        Test if load_from_file behaves as expected
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(
            list_rectangles_output[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(
            list_rectangles_output[1].to_dictionary(), r2.to_dictionary())

    def test_save_to_file(self):
        """
        Test if save_to_file behaves as expected
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                [r1.to_dictionary(), r2.to_dictionary()],
                eval(f.read()))


if __name__ == "__main__":
    unittest.main()
