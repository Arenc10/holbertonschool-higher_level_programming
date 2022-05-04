#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        num = sum(tup[0] * tup[1] for tup in my_list)
        denom = sum(tup[1] for tup in my_list)
        return num / denom
    return 0
