#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ''
    x = 0
    for i in str:
        if x != n:
            str1 = str1 + i
            x += 1
        else:
            x += 1
    return str1
