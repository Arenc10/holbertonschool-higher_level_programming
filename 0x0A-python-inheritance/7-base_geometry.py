#!/usr/bin/python3
""" Defines an empty class named BaseGeometry"""


class BaseGeometry:
    """Method that raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    """Method that validates an integer"""
    def integer_validator(self, name, value):
        self.name = name
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
