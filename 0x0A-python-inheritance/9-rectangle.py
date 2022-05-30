#!/usr/bin/python3
""" Importing a module named BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """__init__ - Initializing Rectangle class
        Args:
            width (int) - Width of the Rectangle
            height (int) - Height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of a Rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns the following string description"""

        return f"[Rectangle] {self.__width}/{self.__height}"
