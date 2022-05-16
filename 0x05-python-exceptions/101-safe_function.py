#!usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as error:
        result = None
        sys.stderr.write("Exception: {}\n".format(error))
    return result
