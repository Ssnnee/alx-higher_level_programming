#!/usr/bin/python3
"""This module contains functions for understanding I/O in python"""
import json


def load_from_json_file(filename):
    """This function creates an Object from a “JSON file”:"""
    with open(filename, encoding="utf-8") as file:
        data = file.read()

    return json.loads("{}".format(data))
