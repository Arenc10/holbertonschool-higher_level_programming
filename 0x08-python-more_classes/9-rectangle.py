#!/usr/bin/python3
"""Rectangle create"""


class Rectangle:
    """Rectangle classs created with width and height
    Attributes:
        number_of_instances (int): the number of instances created and deleted
        print_symbol (any type): symbol for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ __init__ - initalize rectangle class
            Args:
                width (int): The width of a rectangle
                height (int): The height of a rectangle
        """

        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the value for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an int")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Function that compares two rectangles"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __str__(self):
        """Function that uses __str__ method"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        prnt = ""
        for i in range(self.__height):
            for j in range(self.__width):
                prnt += str(self.print_symbol)
            if i < self.__height - 1:
                prnt += '\n'
        return prnt

    def __repr__(self):
        """Return the string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Function that deletes an instance of class"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
