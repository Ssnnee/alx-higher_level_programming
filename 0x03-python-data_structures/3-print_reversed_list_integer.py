#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse_list = my_list[::-1] 
    if my_list is None:
        return
    for i in reverse_list:
        print("{:d}".format(i))
