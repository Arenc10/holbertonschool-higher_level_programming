#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpylist = my_list.copy()
    if idx < 0 or idx not in range(len(my_list)):
        return cpylist
    else:
        cpylist[idx] = element
        return cpylist
