#!/usr/bin/python3
"""This module contains a useful class for understanding inheritance"""


class Rectangle(BaseGeometry):
    """This class is a rectangle that inherits from BaseGeometry"""


    BaseGeometry = __import__("7-base_geometry").BaseGeometry
    def __init__(self, width, height) -> None:
        """This method initializes a new rectangle instance."""

        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
