#!/usr/bin/python3
"""creating an empty class BaseGeometry and adding
Public instance method"""


class BaseGeometry():
    """class BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
