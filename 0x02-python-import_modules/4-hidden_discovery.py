#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    prefix = "__"
    for el in dir(hidden_4):
        if "__" not in el:
            print(el)
