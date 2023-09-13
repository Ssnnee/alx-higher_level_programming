#!/usr/bin/python3
"""This module contains a script that adds all arguments
to a Python list, and then save them to a file"""
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def main():
    """This is the main function of the script"""

    filename = "add_item.json"

    try:
        list_loaded_data = load_from_json_file(filename)
    except Exception:
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write("[]")
        list_loaded_data = load_from_json_file(filename)

    list_args_to_add = list_loaded_data + sys.argv[1:]

    save_to_json_file(list_args_to_add, filename)


main()
