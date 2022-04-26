#!/usr/bin/python3
for first_num in range(10):
    for second_num in range(10):
        if second_num <= first_num:
            continue
        elif first_num != 8 or second_num != 9:
            print('{}{}'.format(first_num, second_num), end=", ")
        else:
            print('{}{}'.format(first_num, second_num))
