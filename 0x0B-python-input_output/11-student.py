#!/usr/bin/python3
"""This module contains a class for understanding json"""


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

    def to_json(self, attrs=None):
        """This method retrieves a dictionary representation of
        a Student instance"""

        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            my_dic = {attr: getattr(self, attr, None) for attr in attrs}
            new = {}

            for key, value in my_dic.items():
                if value is not None:
                    new.update({"{}".format(key): "{}".format(value)})
            return new
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """This methods replaces all attributes of the Student instance"""

        self.__dict__ = json
        return self.__dict__
