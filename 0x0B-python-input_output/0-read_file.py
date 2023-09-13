#!/usr/bin/python3
"""This module contains functions for understanding I/O in python"""


def read_file(filename=""):
    """This functions reads a text file (UTF8) and prints it to stdout"""

    with open(filename, encoding="utf-8") as file:
        data = file.read()

    print(data)
