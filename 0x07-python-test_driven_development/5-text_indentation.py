#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of
    of these character: ., ? and :
    Raise:
        raises TypeError if text is not a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")
    check_space = True
    for char in text:
        if check_space is True and char == " ":
            continue
        check_space = False
        print(char, end="")
        if char in ["?", ".", ":"]:
            check_space = True
            print("\n")
