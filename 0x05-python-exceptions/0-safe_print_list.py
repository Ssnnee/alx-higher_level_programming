#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    cnt = 0
    for i, value in enumerate(my_list):
        if i < x:
            try:
                print(value, end="")
                cnt += 1
            except IndexError:
                break
    print()
    return cnt
