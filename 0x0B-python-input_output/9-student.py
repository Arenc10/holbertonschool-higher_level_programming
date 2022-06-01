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

    def to_json(self):
        """Get a dictionary representation of Student class"""
        return self.__dict__

