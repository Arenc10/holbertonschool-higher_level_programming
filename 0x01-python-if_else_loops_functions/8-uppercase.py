#!/usr/bin/python3
def uppercase(str):
    result = ''
    for letter in str:
        if ord(letter) >= 97 and ord(letter) < 123:
            result = result + chr(ord(letter) - 32)
        else:
            result = result + letter
    print('{}'.format(result))
