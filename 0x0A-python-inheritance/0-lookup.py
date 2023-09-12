#!/usr/bin/python3

"""This module contains a useful function for inheritance"""


def lookup(obj):
    """
    This function returns the list of available
    attributes and methods of an object.
    """

    return list(dir(obj))
