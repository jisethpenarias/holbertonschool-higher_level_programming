#!/usr/bin/python3
"""function that returns True if the object is exactly an
instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Returns is an object is an instance of a_class"""
    # type returns the type of the object class passed: <class 'int'>
    # that allow us to compare with a class:  clase a_class
    return type(obj) == a_class
