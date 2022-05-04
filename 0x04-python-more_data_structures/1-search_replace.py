#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    return [replace if element == search else element for element in new]
