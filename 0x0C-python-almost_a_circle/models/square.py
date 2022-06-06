#!/usr/bin/python3
"""Defining a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square initialized inherits from Rectangle class"""
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

    @property
    def size(self):
        """Getter function"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter function"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""

        argName = ["id", "size", "x", "y"]

        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, argName[i], args[i])
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns a dictionary representation of the Square class"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """Function that returns a string representation of the square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
