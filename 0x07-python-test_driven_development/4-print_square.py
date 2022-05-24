#!/usr/bin/python3
"""Print square based on length"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size (int): length of the square
    Raise:
        raises a TypeError if size is not an int
        raises a ValueError if size is less than 0
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(size):
        for cols in range(size):
            print("#", end="")
        print("")
