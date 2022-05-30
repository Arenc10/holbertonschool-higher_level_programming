#!/usr/bin/python3
""" Defining a MyList class that inherits from the list class"""


class MyList(list):
    """Implements a function that prints a sorted list"""

    def print_sorted(self):
        """Prints a sorted list of integers"""

        print(sorted(self))
