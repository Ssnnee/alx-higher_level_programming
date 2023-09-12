#!/usr/bin/python3

"""This module contains a useful function for understanding inheritance"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This class is a rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height) -> None:
        """This method initializes a new rectangle instance."""

        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the rectangle area"""

        res = self.__height * self.__width
        return res

    def __str__(self) -> str:
        """This method is the toString method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
