#!/usr/bin/python3
"""This module contains functions for understanding I/O in python"""
import json


def from_json_string(my_str):
    """This function convert a JSON string to object"""

    return json.loads(my_str)
