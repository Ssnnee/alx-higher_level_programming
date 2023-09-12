#!/usr/bin/python3

"""This module contains a useful function for understanding inheritance"""


class BaseGeometry:
    """This class is with somes methods"""

    def area(self):
        """This function is not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates the value"""

        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
