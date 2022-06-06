#!/usr/bin/python3
"""Defines a base module"""
import json
from os import path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representations of a obj"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that writes the json string representation to a file"""
        lst = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for el in list_objs:
                lst.append(el.to_dictionary())
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Function that returns a json string to dictionary"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Function that updates by adding class method"""
        testInstance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        testInstance.update(**dictionary)
        return testInstance
