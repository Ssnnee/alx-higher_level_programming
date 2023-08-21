#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    divisor = 0
    mul_sum = 0
    for lists in my_list:
        divisor += lists[1]
        mul_sum += lists[1] * lists[0]
    result = mul_sum / divisor
    return result
