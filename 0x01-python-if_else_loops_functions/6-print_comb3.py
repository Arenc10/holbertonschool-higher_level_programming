#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if x <= i:
            continue
        elif i != 8 or x != 9:
            print('{}{}'.format(i, x), end=", ")
        else:
            print('{}{}'.format(i, x))
