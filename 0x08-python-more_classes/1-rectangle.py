#!/usr/bin/python3
"""1-rectangle module"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """constructor method, initializatión attribute width and heigth"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
