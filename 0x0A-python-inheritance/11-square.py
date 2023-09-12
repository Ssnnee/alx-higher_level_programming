#!/usr/bin/python3

"""This module contains a useful function for understanding inheritance"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a square.
    And inherits from Rectangle
    """

    def __init__(self, size) -> None:
        self.integer_validator("size", size)
        super().__init__(width=size, height=size)
        self.__size = size

    def area(self):
        return super().area()

    def __str__(self) -> str:
        return "[Square] {}/{}".format(self.__size, self.__size)
