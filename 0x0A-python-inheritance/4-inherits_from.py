#!/usr/bin/python3
""" Defining a function that checks instance and type"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of obj
    Returns:
        if obj is an inherited instance of a_class True else False
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
