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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
