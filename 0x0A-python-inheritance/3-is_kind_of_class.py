#!/usr/bin/python3
"""function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """Returns if an object is a kind of a class"""
    # isinstance() to check an instance’s type will be True only if
    # obj.__class__ is a_class or some class derived from a_class.
    return isinstance(obj, a_class)
