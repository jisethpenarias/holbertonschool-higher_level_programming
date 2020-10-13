#!/usr/bin/python3
"""
Unittest from models/base.py
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


# TestBase class, children of TestCase class from the package unittest
class TestBase(unittest.TestCase):
    """unittest TestBase"""

    def test_no_id(self):
        """test case looking if the id is none"""
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_id(self):
        """test case looking if the id is not none"""
        b2 = Base(123)
        self.assertEqual(b2.id, 123)

    def test_id_string(self):
        """test case for set an strubg value to an id"""
        b3 = Base("hello")
        self.assertEqual(b3.id, "hello")

    def test_id_array(self):
        """test case for set an array value to an id"""
        b4 = Base([1, 2, 3])
        self.assertEqual(b4.id, [1, 2, 3])

    def test_negative(self):
        """ test case for set a negative value to an id"""
        b5 = Base(-234)
        self.assertEqual(b5.id, -234)

    def test_not_consecutive(self):
        """ test case looking for assertNotEquals
        1 when you do a second called without arguments
        to the init method"""
        b6 = Base()
        self.assertNotEqual(b6.id, 1)

    def test_string_to_file(self):
        """ test JSON string representation generated on file"""
        x1 = "[{\"height\": 7, \"id\": 3, \"width\": 10, \"x\": 2, \"y\": 8},"
        x2 = "{\"height\": 4, \"id\": 4, \"width\": 2, \"x\": 0, \"y\": 0}]"
        x3 = x1 + x2
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(),  x3)
