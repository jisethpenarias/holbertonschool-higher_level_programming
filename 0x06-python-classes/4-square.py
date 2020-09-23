#!/usr/bin/python3
"""0-square module"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """class builder"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """instance method"""
        return self.__size ** 2
