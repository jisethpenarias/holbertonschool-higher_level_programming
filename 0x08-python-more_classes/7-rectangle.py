#!/usr/bin/python3
"""6-rectangle module"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method width"""
        return self.__width

    @width.setter
    def width(self, value_width):
        """setter method width"""
        if type(value_width) is not int:
            raise TypeError("width must be an integer")
        if value_width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value_width

    @property
    def height(self):
        """getter method height"""
        return self.__height

    @height.setter
    def height(self, value_height):
        if type(value_height) is not int:
            raise TypeError("height must be an integer")
        if value_height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value_height

    def area(self):
        """instance method"""
        return self.width * self.height

    def perimeter(self):
        """instance method"""
        # using the attributes intialized on the init method..directly
        if self.width is 0 or self.height is 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """new implementation of str method prints with the character #"""
        string = ""
        if self.width is 0 or self.height is 0:
            return string
            # return ""
        else:
            # for i in range(self.__height):
                # for x in range(self.__width):
                    # print("#", end="")
                # if i != (self.__height - 1):
                    # print("")
            # return ""
            # the previous lines also work
            for i in range(self.height):
                for x in range(self.width):
                    string = string + str(self.print_symbol)
                string = string + '\n'
            return string[:-1]

    def __repr__(self):
        """implementation of repr method

        Return: a string representation of the rectangle to be able
        to recreate a new instance by using eval() (Rectangle(2, 4))"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    # Deleting (Calling destructor)
    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
