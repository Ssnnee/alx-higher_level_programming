#!/usr/bin/python3

"""This module contains a useful function for understanding inheritance"""


def inherits_from(obj, a_class):
    """ "This function  returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    if obj is None:
        return False

    if not type(obj) is a_class:
        return issubclass(type(obj), a_class)
