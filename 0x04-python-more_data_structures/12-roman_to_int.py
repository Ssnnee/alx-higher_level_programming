#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    my_list = []
    for i in range(1, 10000000):
        my_list.append(i)

    if roman_string in my_list:
        return "None"

    int_number = 0
    for n in roman_string:
        for k in dic:
            if n == k:
                n = dic[k]
                int_number += dic[k]

    return int_number
