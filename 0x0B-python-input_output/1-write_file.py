#!/usr/bin/python3
"""This module contains functions for understanding I/O in python"""


def write_file(filename="", text=""):
    """This function  writes a string to a text file (UTF8)
    and returns the number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        written_dat = file.write(text)
    return written_dat
