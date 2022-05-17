#!/usr/bin/python3
"""Define a class Square"""
class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """
        Initalize a new square.

        Args:
        size (int): The size of the new square
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
            """Return the current area of the square."""
        return self.__size * self.__size
