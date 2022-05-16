#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for el in range(list_length):
        try:
            res = my_list_1[el] / my_list_2[el]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except (ValueError, TypeError):
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            new_list.append(res)
    return new_list
