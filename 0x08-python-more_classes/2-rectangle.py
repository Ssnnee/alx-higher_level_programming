#!/usr/bin/python3
"""
This module contains Simple rectangle class with property and some methods
"""


class Rectangle:
    """This class is an empty class that defines a rectangle"""

    def __init__(self, width=0, height=0) -> None:
        """Initializes a new rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Allow width to be set"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Allow height to be set"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the rectangle area"""
        res = self.height * self.width
        return res

    def perimeter(self):
        """Return the perimeter of the retangle"""
        res = (self.height + self.width) * 2
        return res
