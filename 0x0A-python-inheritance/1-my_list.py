#!/usr/bin/python3

"""This module contains a useful function for understanding inheritance"""


class MyList(list):
    """This class is a child of list class"""

    def print_sorted(self):
        """This function prints a sorted list."""
        print(sorted(self)))
