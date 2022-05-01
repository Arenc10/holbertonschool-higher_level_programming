#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    if 0 <= idx < len(my_list):
        cpylist = my_list.copy()
        cpylist[idx] = element
        return cpylist

