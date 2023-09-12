#!/usr/bin/python3
""" This module contains a class that inherits"""


class MyInt(int):
    """This class inherits from int with reveted ed and ne operators"""

    def __eq__(self, other):
        """Invert the == operator"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Invert the != operator"""
        return int.__eq__(self, other)
