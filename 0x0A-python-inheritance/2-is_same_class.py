#!/usr/bin/python3
"""Defining a function checking the class instance"""


def is_same_class(obj, a_class):
    """Returns True if the objecs is an instance of the class lese False"""

    return type(obj) is a_class
