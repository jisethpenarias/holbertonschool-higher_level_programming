#!/usr/bin/python3
"""0-square module"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """class builder"""
        self.__size = size

    # gets the value of the variable on the instance
    @property
    def size(self):
        """getter method"""
        return self.__size

    # setter change value of the variable on the instance
    @size.setter
    def size(self, value):
        """setter method"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """instance method"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print("")
