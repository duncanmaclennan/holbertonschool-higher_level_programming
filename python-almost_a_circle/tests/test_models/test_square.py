#!/usr/bin/python3
"""Module for testing Square class"""
import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test methods of SquareClass"""

    def setUp(self):
        """reset the base class private attribute"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """clean up the class private attribute"""
        Base._Base__nb_objects = None

    def test_init_with_valid_inputs(self):
        """Test init method"""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.id, 1)

        s2 = Square(1, 2)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.id, 2)

        s2 = Square(1, 2, 3)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 3)

        s3 = Square(1, 2, 3, 4)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 4)

    def test_init_with_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Square("Pikachu", 7, 7)
        with self.assertRaises(TypeError):
            Square(7, "Pikachu", 7)
        with self.assertRaises(TypeError):
            Square(7, 7, "Pikachu")
        with self.assertRaises(ValueError):
            Square(-7, 7, 7)
        with self.assertRaises(ValueError):
            Square(7, -7, 7)
        with self.assertRaises(ValueError):
            Square(7, 7, -7)
        with self.assertRaises(ValueError):
            Square(0, 7, 7)

    def test_str(self):
        """test the str method"""
        prt_str1 = Square(3, 4, 5, 33)
        self.assertEqual(str(prt_str1), "[Square] (33) 4/5 - 3")
        prt_str2 = Square(3, 0)
        self.assertEqual(str(prt_str2), "[Square] (1) 0/0 - 3")

    def test_update(self):
        """Test update"""
        s1 = Square(1, 2, 3, 4)
        s1.update(7)
        self.assertEqual(s1.id, 7)

        s2 = Square(1, 2)
        s2.update()
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)

    def test_to_dictionary(self):
        """Testing to_dictionary()"""
        s1 = Square(1, 2, 3, 4)
        result = s1.to_dictionary()
        self.assertEqual(result, {"id": 4, "size": 1, "x": 2, "y": 3})

    def test_create(self):
        """Test create"""
        s1 = Square.create(**{'id': 3, 'size': 1, 'x': 3, 'y': 4})
        expect = "[Square] (3) 3/4 - 1"
        self.assertEqual(str(s1), expect)

    def test_save_to_file(self):
        """Test save to file"""
        Square.save_to_file(None)
        with open("Square.json", "r") as t_file:
            self.assertEqual(t_file.read(), "[]")
            os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as t_file:
            self.assertEqual(t_file.read(), "[]")
            os.remove("Square.json")

        Square.save_to_file([Square(1, 2)])
        with open("Square.json", "r") as t_file:
            expect = '[{"id": 1, "size": 1, "x": 2, "y": 0}]'
            self.assertEqual(t_file.read(), expect)
            os.remove("Square.json")

    def test_from_json(self):
        """Test load from file"""
        s1 = Square(1)
        s2 = Square(3)
        list_of_objs = [s1, s2]
        Square.save_to_file(list_of_objs)

        result_list = Square.load_from_file()
        self.assertTrue(len(result_list) == 2)
        self.assertTrue(result_list[0].size == 1)
        self.assertTrue(result_list[1].size == 3)
        os.remove("Square.json")
