#!/usr/bin/python3
""" Module that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers """
    to_return = None
    for i in range(0, len(list_of_integers) - 1):
        if list_of_integers[i] >= list_of_integers[i + 1]:
            to_return = list_of_integers[i]
    return to_return
