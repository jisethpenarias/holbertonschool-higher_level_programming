#!/usr/bin/python3
"""
Unittest for models/rectangle.py
"""


import unittest
import sys
from io import StringIO

from models.base import Base
from models.rectangle import Rectangle


# TestRectangle class, children of TestCase class from the package unittest
class TestRectangle(unittest.TestCase):
    """
    unittest TestRectangle
    """

    def setUp(self):
        """ Before test, preparing scenario"""
        sys.stdout = StringIO()

    def tearDown(self):
        """ After test, cleaning variables used on setUp method"""
        sys.stdout = sys.__stdout__

    def test_inherintance(self):
        """ test case for showing inheritance """
        rect1 = Rectangle(1, 1)
        self.assertTrue(issubclass(rect1.__class__, Base))

    def test_width_none_parameter(self):
        """ test case for sending None parameter to width """
        with self.assertRaises(TypeError) as te:
            Rectangle(None, 1)
        self.assertEqual(str(te.exception), "width must be an integer")

    def test_height_none_parameter(self):
        """ test case for sending None parameter to height """
        with self.assertRaises(TypeError) as te:
            Rectangle(1, None)
        self.assertEqual(str(te.exception), "height must be an integer")

    # test cases sending String parameters for Numeric values
    def test_string_x_parameter(self):
        """ test case for string x"""
        with self.assertRaises(TypeError) as te:
            Rectangle(1, 1, "x", 1)
        self.assertEqual(str(te.exception), "x must be an integer")

    def test_string_y_parameter(self):
        """ test case for string y"""
        with self.assertRaises(TypeError) as te:
            rect = Rectangle(1, 1, 1, "y")
        self.assertEqual(str(te.exception), "y must be an integer")

    def test_string_width_parameter(self):
        """ test case for string width"""
        with self.assertRaises(TypeError) as te:
            rect = Rectangle("width", 1, 1, 1)
        self.assertEqual(str(te.exception), "width must be an integer")

    def test_string_height_parameter(self):
        """ test case for string  height"""
        with self.assertRaises(TypeError) as te:
            rect = Rectangle(1, "height", 1, 1)
        self.assertEqual(str(te.exception), "height must be an integer")

    # test cases that send negative numbers
    def test_negative_num_x_parameter(self):
        """ test case for negative x"""
        with self.assertRaises(ValueError) as ve:
            Rectangle(1, 1, -1, 1)
        self.assertEqual(str(ve.exception), "x must be >= 0")

    def test_negative_num_y_parameter(self):
        """ test case for negative y"""
        with self.assertRaises(ValueError) as ve:
            rect = Rectangle(1, 1, 1, -1)
        self.assertEqual(str(ve.exception), "y must be >= 0")

    def test_negative_num_width_parameter(self):
        """ test case for negative width"""
        with self.assertRaises(ValueError) as ve:
            rect = Rectangle(-1, 1, 1, 1)
            self.assertEqual(str(ve.exception), "width must be >= 0")

    def test_negative_num_height_parameter(self):
        """ test case for negetive height"""
        with self.assertRaises(ValueError) as ve:
            rect = Rectangle(1, -1, 1, 1)
            self.assertEqual(str(ve.exception), "height must be >= 0")

    # test cases that send float numbers
    def test_float_x_parameter(self):
        """ test case for float x"""
        with self.assertRaises(TypeError) as te:
            Rectangle(1, 1, 2.5, 1)
        self.assertEqual(str(te.exception), "x must be an integer")

    def test_float_y_parameter(self):
        """ test case for float y"""
        with self.assertRaises(TypeError) as te:
            rect = Rectangle(1, 1, 1, 2.5)
        self.assertEqual(str(te.exception), "y must be an integer")

    def test_float_width_parameter(self):
        """ test case for float width"""
        with self.assertRaises(TypeError) as te:
            rect = Rectangle(2.5, 1, 1, 1)
        self.assertEqual(str(te.exception), "width must be an integer")

    def test_float_height_parameter(self):
        """ test case for float height"""
        with self.assertRaises(TypeError) as te:
            rect = Rectangle(1, 2.5, 1, 1)
        self.assertEqual(str(te.exception), "height must be an integer")

    # test cases for area
    def test_calc_area(self):
        """ test case for calc area method"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    # test cases for print
    def test_print_big(self):
        """ test case for print rectangle big"""
        rec1 = Rectangle(2, 5)
        str_rec1 = "##\n" \
                   "##\n" \
                   "##\n" \
                   "##\n" \
                   "##\n"
        try:
            rec1.display()
            self.assertEqual(sys.stdout.getvalue(), str_rec1)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_print_whit_xy(self):
        """ test case for  print rectangle with x and y"""
        rec3 = Rectangle(3, 2, 1, 0)
        str_rec3 = " ###\n" \
                   " ###\n"
        try:
            rec3.display()
            self.assertEqual(sys.stdout.getvalue(), str_rec3)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_overrinding_str(self):
        """Test case for string representation"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        str_r1_representation = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(r1.__str__(), str_r1_representation)

    def test_overrinding_str02(self):
        """Test case for string representation"""
        r2 = Rectangle(5, 5, 1)
        str_r2_representation = "[Rectangle] (13) 1/0 - 5/5"
        self.assertEqual(r2.__str__(), str_r2_representation)

    def test_update(self):
        """Test case for update"""
        rec = Rectangle(10, 2, 3, 4, 1)
        rec.update(89)
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 3/4 - 10/2")

    def test_update_kwargs(self):
        """Test case for update with dict."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 3/1 - 2/1")

    def test_invalid_kwargs(self):
        """Test case for kwargs that do not match attributes."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(weight=25)
        self.assertEqual(hasattr(r, 'weight'), False)

    def test_dict(self):
        """Test case rectangle dictionary representation"""
        rec = Rectangle(10, 2, 3, 4, 5)
        rec_dictionary = {'width': 10, 'height': 2, 'x': 3, 'id': 5, 'y': 4}
        self.assertEqual(rec.to_dictionary(), rec_dictionary)
        self.assertEqual(rec.to_dictionary() is rec_dictionary, False)

    def test_to_json_string(self):
        """Test case list of rectangle json representation"""
        x = "[{\"height\": 7, \"id\": 20, \"width\": 10, \"x\": 2, \"y\": 8}]"
        rectangle_to_json = Rectangle(10, 7, 2, 8)
        dictionary = rectangle_to_json.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, x)

    def test_to_json_string_none(self):
        """Test case none rectangle json representation"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")
