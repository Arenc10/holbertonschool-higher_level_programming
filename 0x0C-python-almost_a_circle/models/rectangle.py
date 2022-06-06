#!/usr/bin/python3
""" Defining a rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class created that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ - Initializing Rectangle class with its args

        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
            x (int): x
            y (int): y
            id (int): Id number of obj
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter function for width"""
        return self.__width

    @property
    def height(self):
        """Getter function for height"""
        return self.__height

    @property
    def x(self):
        """Getter function for x"""
        return self.__x

    @property
    def y(self):
        """Getter function for y"""
        return self.__y

    @width.setter
    def width(self, width):
        """Setter function for width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Setter function for height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """Setter function for x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """Setter function for y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Function that gets the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Function that will display a rectangle with #"""
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        """Str representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """Function that updates dhe value for keys"""
        argNames = ["id", "width", "height", "x", "y"]

        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, argNames[i], args[i])
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Function that returns dictionary representation Rectangle class"""
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
