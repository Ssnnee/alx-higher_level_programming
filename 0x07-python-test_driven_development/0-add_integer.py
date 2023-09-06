#!/usr/bin/python3
"""
This module contains an integers additionor function
"""


def add_integer(a, b=98):
    """This function adds 2 integers."""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        a = int(a)
        b = int(b)
        res = a + b
        return res
    else:
        raise TypeError("a must be an integer or b must be an integer")
