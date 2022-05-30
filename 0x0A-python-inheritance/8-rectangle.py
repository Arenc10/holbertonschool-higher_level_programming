#!/usr/bin/python3
""" Defines an empty class named BaseGeometry"""


class BaseGeometry:
    """Method that raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")

    """Method that validates an integer"""
    def integer_validator(self, name, value):
        """ Validates value
        Args:
            name (str): string
            value (int): integer
        Raise:
            raises TypeError if value is not int
            raises ValueError if is less or equal than 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
