#!/usr/bin/python3
"""
New Rectangle class that inherits from the Base class
"""


from models.base import Base
import sys


class Rectangle(Base):
    """This class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the attributes of the rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ recuperar y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """instance area method"""
        return self.__width * self.__height

    def display(self):
        """instance method that prints"""
        string = ""
        if self.width is 0 or self.height is 0:
            return string
        else:
            if self.y >= 0:
                for y in range(self.y):
                    string = string + str("\n")
            for i in range(self.height):
                if self.y >= 0:
                    for x in range(self.x):
                        string = string + str(" ")
                for a in range(self.width):
                    string = string + str("#")
                string = string + '\n'
            print(string[:-1])

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute"""
        if args is not None:
            attributes = ["id", "width", "height", "x", "y"]
        # para (posicion , valor) en la enumeracion de args
            for idx, arg in enumerate(args):
                setattr(self, attributes[idx], arg)
        for key, value in kwargs.items():
            # hasattr() function returns True if the specified object has the
            # specified attribute, otherwise False.
            # hasattr(object, attribute)
            if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        key_atributes = ["id", "width", "height", "x", "y"]
        # dict() creates a dictionary.
        # dict(keyword arguments)
        dic_atributes = dict()
        for key_attr in key_atributes:
            # getattr() method returns the value of the named attribute of
            # an object.
            # If not found, it returns the default value provided to the
            # function.
            # getattr(object, name[, default])
            # getattr(self, atrr...) - getattr(self, key_attr)
            # getattr(self, atrr, "{} no encontrado".format(atrr))-
            # it was not used

            dic_atributes[key_attr] = getattr(self, key_attr)
        return dic_atributes
