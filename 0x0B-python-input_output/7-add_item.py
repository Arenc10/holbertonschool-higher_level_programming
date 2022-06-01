#!/usr/bin/python3
"""Imports the necessary modules and adds arguments in a json string"""

import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argLs = []
if os.path.exists("add_item.json"):
    argLs = load_from_json("add_item.json")
save_to_json_file(argList + sys.argv[1:], "add_item.json")
