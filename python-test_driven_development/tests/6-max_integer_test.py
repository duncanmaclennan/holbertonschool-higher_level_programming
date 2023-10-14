#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test for max integer"""

    def test_max_pos_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_neg_int(self):
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def test_descending(self):
        self.assertEqual(max_integer([3, 2, -1, -3]), 3)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_int(self):
        self.assertEqual(max_integer([1]), 1)
