#!/usr/bin/python3
"""This module is a preparation for technical interview
not allow to google anything
"""


def pascal_triangle(n):
    """This function returns a list of lists of integers
    representing the Pascal’s triangle of n"""

    if n <= 0:
        return list([])

    m = 0
    triangle_dic = {}

    while m < n + 1:
        triangle_dic.update({"{}".format(m): []})
        m += 1
    my_list = list([])
    last_op = 1
    ml = 1

    for key, itms in triangle_dic.items():
        if key == "0":
            itms.append(1)
            my_list = itms[:]

        elif key > "0":
            itms.append(1)
            mn = int(key)

            for op in my_list:
                if mn > ml:
                    itms.append(last_op + op)
                    ml += 1
                last_op = op
            itms.append(1)

    my_lists = []
    for _ in triangle_dic:
        my_lists.append(triangle_dic[_])

    return my_lists
