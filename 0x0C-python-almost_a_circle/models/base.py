#!/usr/bin/python3
"""Defining a Base class"""


class Base:
    """ Base class

    Attributes:
        __nb_objects (int): Number of objects created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ - initalizes the base class

        Args:
            id (int): Id of the object
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
