#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
        size (int): The size of the new square.
        """
        self.size = size
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) not int:
        raise TypeError("size must be an integer")
