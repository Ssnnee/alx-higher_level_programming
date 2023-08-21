#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete_list = []
    for keys, values in a_dictionary.items():
        if values == value:
            to_delete_list.append(keys)

    for key in to_delete_list:
        del a_dictionary[key]

    return a_dictionary
