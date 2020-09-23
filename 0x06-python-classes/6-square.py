#!/usr/bin/python3
"""0-square module"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """class builder"""
        self.__size = size
        self.__position = position

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
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for x in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method for position"""
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
