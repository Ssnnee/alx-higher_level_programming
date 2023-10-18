#!/usr/bin/python
"""This module contains some useful classes or function for OOP"""


class Base(object):
    """This class is the base for all classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """This method initializes a new rectangle instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
