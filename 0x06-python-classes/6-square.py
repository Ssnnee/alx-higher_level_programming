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

    def __init__(self, size=0, position=(0, 0)) -> None:
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
            position(tuple):
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Retrieve the position

        Returns:
            The value of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Allow the position to be set

        Args:
            value: The position value to be set.
        """
        if all(i > 0 for i in value) and  len(value) == 2:
            self.__position = value
        raise TypeError("position must be a tuple of 2 positive integers")

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
