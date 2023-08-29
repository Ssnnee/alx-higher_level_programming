#!/usr/bin/python3

"""
This module defines a Square class.
"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0) -> None:
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size

    @property
    def __size(self):
        """
        Retrieve the size

        Returns:
            The value of size
        """
        return self.__size_value

    @__size.setter
    def __size(self, value):
        """
        Allow the size to be set

        Args:
            value: The size value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size_value = value
