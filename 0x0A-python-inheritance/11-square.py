#!/usr/bin/python3
""" Importing rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits Rectangle"""

    def __init__(self, size):
        """__init__ - Initialize of the Square class

        Args:
            size (int) - Size of the Square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the Square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns the description for the Square"""

        return f"[Square] {self.__size}/{self.__size}"
