#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Prints the text of a file to stdout using with keyword"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
