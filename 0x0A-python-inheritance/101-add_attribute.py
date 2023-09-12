#!/usr/bin/python3
"""This module contains a useful function for understanding inheritance"""


def add_attribute(obj, attribute_to_add, value):
    """This function adds a new attribute to an object if it's possible.
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, attribute_to_add, value)
    else:
        raise TypeError("can't add new attribute")
