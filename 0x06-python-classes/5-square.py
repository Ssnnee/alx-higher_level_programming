#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This class defines a square.

    Attributes:
        _size (int): The size of the square.
    """

    def __init__(self, size=0) -> None:
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size

        Returns:
            The value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Allow the size to be set

        Args:
            value: The size value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the square area

        Return:
            (int):The value of area
        """
        return self.__size * self.__size

    def my_print(self):
        """This method prints in stdout the square with the character #"""
        if self.__size == 0:
            print()

        cols = self.__size
        rows = self.__size
        matrix = [["#" for _ in range(cols)] for _ in range(rows)]
        for row in matrix:
            print("".join(row))

