#!/usr/bin/python3
"""This module is a preparation for technical interview
not allow to google anything
"""

""" I did not passes the interview test here the right function"""
def pascal_triangle(n):
    """This function returns a list of lists of integers
    representing the Pascal’s triangle of n"""

    if n <= 0:
        return list([])

    triangle_dic = {}

    for m in range(n + 1):
        triangle_dic[m] = []

    last_number = 0

    for key in range(n + 1):
        triangle_dic[key].append(1)
        if key > 0:
            for _ in range(1, key):
                new_number = (
                    triangle_dic[key - 1][last_number]
                    + triangle_dic[key - 1][last_number + 1]
                )
                triangle_dic[key].append(new_number)
                last_number += 1
            triangle_dic[key].append(1)
            last_number = 0

    return [v for k, v in sorted(triangle_dic.items())]
