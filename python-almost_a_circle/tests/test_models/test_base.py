#!/usr/bin/python3
"""Test Module"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test methods of BassClass"""

    def setUp(self):
        """Runs for each test reset private attribute"""
        Base._Base__nb_objects = 0

    def test_init_none_id(self):
        """Test none_id passed in"""
        base0 = Base()
        self.assertEqual(base0.id, 1)

    def test_init_id_passed(self):
        """Test whether Base returns id if a number passed in"""
        base = Base(7)
        self.assertEqual(base.id, 7)

    def test_init_increm_id(self):
        """Test whether incremental works none_id passed in"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_json_string_with_none(self):
        """Test Json string with None passed in"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_json_string_with_empty_list(self):
        """Test Json string with None passed in"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_json_string_with_dict_list(self):
        """Test Json string with valid dict_list"""
        list_input = [{'id': 89}, {'width': 10}]
        self.assertEqual(Base.to_json_string(list_input),
                         '[{"id": 89}, {"width": 10}]')
