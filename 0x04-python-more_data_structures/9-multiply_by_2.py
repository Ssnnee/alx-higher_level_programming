#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for k, i in new_dic.items():
        new_dic[k] = i*2
    return new_dic
