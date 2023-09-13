#!/usr/bin/python3
"""This module contains functions for understanding I/O in python"""


class Student:
    """This class defines a student"""

    def __init__(self, first_name, last_name, age) -> None:
        """This method initiates a Student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method etrieves a dictionary representation of
        a Student instance"""

        return self.__dict__
