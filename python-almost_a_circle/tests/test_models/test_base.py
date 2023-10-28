import unittest

from models.base import Base


class TestBase (unittest.TestCase):
    """
    Test cases for Base
    """

    def test_assign_id(self):
        """
        Test if Base assigns unique ID
        """
        b0 = Base()
        b1 = Base()
        self.assertNotEqual(b0.id, b1.id)

    def test_assign_next_id(self):
        """
        Test if Base assigns id that is +1 from previous id (if is exists)
        """
        b0 = Base()
        b1 = Base()
        b2 = Base()
        self.assertEqual(b0.id + 1, b1.id)
        self.assertEqual(b1.id + 1, b2.id)

    def test_save_id(self):
        """
        Test if Base saves id
        """
        b = Base(123)
        self.assertEqual(b.id, 123)

    def test_json_str_input(self):
        """
        Test to_json_string returns [] if input None or empty
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string(self):
        """
        Test to_json_string returns JSON string representation of input
        """
        json_input = [{"id": 10}]
        func = Base.to_json_string(json_input)
        self.assertEqual(func, '[{"id": 10}]')

    def test_from_json_str_input(self):
        """
        Test from_json_string returns [] if input None or empty
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_str(self):
        """
        Test from_json_string returns list of JSON string representation
        """
        json_input = '[{"id": 10}]'
        func = Base.from_json_string(json_input)
        self.assertEqual(func, [{"id": 10}])
