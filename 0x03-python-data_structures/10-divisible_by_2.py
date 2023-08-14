#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = my_list[:]
    for items, i in enumerate(my_list):
        if i % 2 == 0:
            list[items] = True
        else:
            list[items] = False

    return list
