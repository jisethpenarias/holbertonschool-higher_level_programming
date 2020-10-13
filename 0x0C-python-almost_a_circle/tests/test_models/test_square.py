#!/usr/bin/python3
"""
Unittest for models/square.py
"""


import unittest
import json

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


# TestSquare class, children of TestCase class from the package unittest
class TestSquare(unittest.TestCase):
    """
    unittest TestSquare
    """

    def test_inherintance(self):
        """ test case for showing inheritance"""
        rect1 = Square(5)
        self.assertTrue(issubclass(rect1.__class__, Rectangle))

    def test_update(self):
        """Test case for update"""
        rec = Square(10, 3, 4, 1)
        rec.update(89)
        self.assertEqual(rec.__str__(), "[Square] (89) 3/4 - 10")

    def test_update_kwargs(self):
        """Test case for update with dict."""
        r = Square(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.__str__(), "[Square] (10) 10/10 - 10")
        r.update(width=1, x=2)
        self.assertEqual(r.__str__(), "[Square] (10) 2/10 - 1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Square] (89) 3/1 - 2")

    def test_invalid_kwargs(self):
        """Test case for kwargs that do not match attributes."""
        r = Square(1, 2, 3, 4)
        r.update(weight=25)
        self.assertEqual(hasattr(r, 'weight'), False)

    def test_dict(self):
        """Test case representation of Square"""
        rec = Square(10, 3, 4, 5)
        rec_dictionary = {'size': 10, 'x': 3, 'id': 5, 'y': 4}
        self.assertEqual(rec.to_dictionary(), rec_dictionary)
        self.assertEqual(rec.to_dictionary() is rec_dictionary, False)
