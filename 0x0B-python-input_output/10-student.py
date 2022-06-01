#!/usr/bin/python3
"""Defines a python Student class"""


class Student:
    """Representing a student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student class

        Args:
            first_name (str): Student first name.
            last_name (str): Student last name.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of Student class"""
        new_dict = {}
        if attrs is None:
            return self.__dict__
        for el in attrs:
            if el in self.__dict__:
                new_dict[el] = self.__dict__[el]
        return new_dict
