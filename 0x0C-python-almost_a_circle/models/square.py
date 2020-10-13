#!/usr/bin/python3
"""
New Square class that inherits from the Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class Square
    Only the parameters that do not have =? example x = 0 or y = 0 or id = None
    Those parameters are not mandatory because when in the __init__ method
    (Constructor Method) the arguments are defined with equal (=) it means that
    if they are not passed in the creation of an instance the default values
    ​​will be the values ​​that are after the equal (=) in the __init__ method

    x & y have 0 values ​​because the default printing should be done at the
    edge of the console.
    id has a default value of None because the creation of the ids is
    controlled in the Base class.

    All the classes that implement the __init__ method are defined by the
    arguments it receives in this case the square class is defined by:
        size (mandatory): parameter that identifies the size of the square
        x (optional): value that defines the position in x in which it will be
        printed in the console.
        y (optional): value that defines the position in and in which it will
        be printed in the console.
        id (optional): value that defines the identifier of the instance that
        is being requested to create."""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing the attributes of the Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading method should return:"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter method"""
        return self.width

    # setter change value of the variable on the instance
    @size.setter
    def size(self, value):
        """setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute"""
        if args is not None:
            attributes = ["id", "size", "x", "y"]
            # para (posicion , valor) en la enumeracion de args
            for idx, arg in enumerate(args):
                # setattr() function is used to set a value to the object's
                # attribute
                # setattr (object, name of the atribute, value)
                if index < 4:
                    setattr(self, attributes[idx], arg)
        for key, value in kwargs.items():
            # hasattr() function returns True if the specified object has the
            # specified attribute, otherwise False.
            # hasattr(object, attribute)
            if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation of a Square"""
        key_atributes = ["id", "size", "x", "y"]
        # dict() creates a dictionary.
        # dict(keyword arguments)
        dic_atributes = dict()
        for key_attr in key_atributes:
            # getattr() method returns the value of the named attribute
            # of an object.
            # If not found, it returns the default value provided
            # to the function.
            # getattr(object, name[, default])
            # getattr(self, atrr...)
            # getattr(self, atrr, "{} no encontrado".format(atrr))
            dic_atributes[key_attr] = getattr(self, key_attr)
        return dic_atributes
