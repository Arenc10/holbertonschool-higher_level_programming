#!/usr/bin/python3
"""Square class"""


class Square:
    """__init__method that initialize square class
    Args:
        size: size of the square
        position: position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the value of attribute size"""

        return self.__size

    @property
    def position(self):
        """Gets the value of attribute position"""

        return self.__position

    @size.setter
    def size(self, value):
        """Sets the value of attribute size"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Sets the value for attribute position"""

        if type(value) != tuple
        or len(value) != 2
        or type(value[0]) != int
        or type(value[1]) != int
        or value[0] < 0
        or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of a square"""

        return self.size * self.size

    def my_print(self):
        """Prints a square how it should be printed regarding errors"""

        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for row in range(self.size):
                print(" " * self.position[0], end="")
                for col in range(self.size):
                    print("#", end="")
                print("")
