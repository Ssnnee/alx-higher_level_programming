#!/usr/bin/python3
"""This module contains functions for understanding I/O in python"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""

    with open(filename, mode="+a", encoding="utf-8") as file:
        appended_char_num = file.write(text)
    return appended_char_num
