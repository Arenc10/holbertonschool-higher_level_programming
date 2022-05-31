#!/usr/bin/python3
"""Defines a Python class to a json function"""


def class_to_json(obj):
    """Return the dictionary representation of a data structre"""
    return obj.__dict__
