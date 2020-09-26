#!/usr/bin/python3

"""
Unit Test for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_one_num(self):
        self.assertEqual(max_integer([3]), 3)

    def test_string(self):
        self.assertEqual(max_integer(['m', 'a', 'x']), 'x')

    def test_ordered_num(self):
        self.assertEqual(max_integer([5, 2, 3, 4]), 5)

    def test_unordered_num(self):
        self.assertEqual(max_integer([2, 7, 1, 3]), 7)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_neg_num(self):
        self.assertEqual(max_integer([-2, -3]), -2)

if __name__ == '__main__':
    unittest.main()
