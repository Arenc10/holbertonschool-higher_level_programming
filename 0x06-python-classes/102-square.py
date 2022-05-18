#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Initialize a new square.
        Args:
            size (int): The size of the new square.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""

        return self.__size * self.__size

    def __eq__(self, other):
        """Return a boolean value comparing two objects"""

        return self.area() == other.area()

    def __ne__(self, other):
        """Return a boolean value comparing two objects"""

        return self.area() != other.area()

    def __lt__(self, other):
        """Return a boolean value comparing two objects"""

        return self.area() < other.area()

    def __gt__(self, other):
        """Return a boolean value comparing two objects"""

        return self.area() > other.area()

    def __le__(self, other):
        """Return a boolean value comparing two objects"""

        return self.area() <= other.area()

    def __ge__(self, other):
        """Return a boolean value comparing two objects"""

        return self.area() >= other.area()
