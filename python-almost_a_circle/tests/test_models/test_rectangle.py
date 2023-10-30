#!/usr/bin/python3
"""Module for testing Rectangle class"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test methods of RectangleClass"""

    def setUp(self):
        """reset the base class private attribute"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """clean up the class private attribute"""
        Base._Base__nb_objects = None

    def test_init_with_valid_inputs(self):
        """Test init method"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.id, 3)

        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.width, 1)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 4)
        self.assertEqual(r4.id, 5)

    def test_init_with_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Rectangle("Pikachu", 7, 7, 7)
        with self.assertRaises(TypeError):
            Rectangle(7, "Pikachu", 7, 7)
        with self.assertRaises(TypeError):
            Rectangle(7, 7, "Pikachu", 7)
        with self.assertRaises(TypeError):
            Rectangle(7, 7, 7, "Pikachu")
        with self.assertRaises(ValueError):
            Rectangle(-7, 7, 7, 7)
        with self.assertRaises(ValueError):
            Rectangle(7, -7, 7, 7)
        with self.assertRaises(ValueError):
            Rectangle(7, 7, -7, 7)
        with self.assertRaises(ValueError):
            Rectangle(7, 7, 7, -7)
        with self.assertRaises(ValueError):
            Rectangle(0, 7, 7, 7)
        with self.assertRaises(ValueError):
            Rectangle(7, 0, 7, 7)

    def test_area(self):
        """test the area method"""
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)

    def test_str(self):
        """test the str method"""
        prt_str1 = Rectangle(3, 4, 2, 5, 33)
        self.assertEqual(str(prt_str1), "[Rectangle] (33) 2/5 - 3/4")
        prt_str2 = Rectangle(7, 1, 0)
        self.assertEqual(str(prt_str2), "[Rectangle] (1) 0/0 - 7/1")

    def test_display(self):
        """Testing display()"""

        o1 = Rectangle(1, 3)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            o1.display()
            self.assertEqual(fakeOutput.getvalue(), '#\n#\n#\n')

        o2 = Rectangle(2, 3, 1, 0)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            o2.display()
            self.assertEqual(fakeOutput.getvalue(), ' ##\n ##\n ##\n')

    def test_to_dictionary(self):
        """Testing to_dictionary()"""

        r1 = Rectangle(1, 2, 3, 4, 5)
        result = r1.to_dictionary()
        self.assertEqual(result, {"id": 5, "width": 1, "height": 2,
                                  "x": 3, "y": 4})

    def test_update(self):
        """Test update"""

        r1 = Rectangle(1, 2, 3, 4, 5)
        r1.update(7)
        self.assertEqual(r1.id, 7)

        r2 = Rectangle(1, 2)
        r2.update()
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)

    def test_create(self):
        """Test create"""

        r1 = Rectangle.create(**{'id': 3, 'width': 1, 'height': 2,
                                 'x': 3, 'y': 4})
        expect = "[Rectangle] (3) 3/4 - 1/2"
        self.assertEqual(str(r1), expect)

    def test_save_to_file(self):
        """Test save to file"""

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as t_file:
            self.assertEqual(t_file.read(), "[]")
            os.remove("Rectangle.json")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as t_file:
            self.assertEqual(t_file.read(), "[]")
            os.remove("Rectangle.json")

        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as t_file:
            expect = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]'
            self.assertEqual(t_file.read(), expect)
            os.remove("Rectangle.json")

    def test_load_from_file(self):
        """Test load from file"""

        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        list_of_objs = [r1, r2]
        Rectangle.save_to_file(list_of_objs)

        result_list = Rectangle.load_from_file()
        self.assertTrue(len(result_list) == 2)
        self.assertTrue(result_list[0].width == 1)
        self.assertTrue(result_list[1].width == 3)
        os.remove("Rectangle.json")
