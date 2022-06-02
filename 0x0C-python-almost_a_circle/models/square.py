#!/usr/bin/python
"""Defining a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ __init__ - Initializes the Square class
        Args:
            size (int): Size of the Square
            x (int): x
            y (int): y
            id (int): The id of object
        """
        super().__init__(size, size, x, y, id)
        self.size = size
        self.size = size
    
    def __str__(self):
        """Function that returns a string representation of Square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
