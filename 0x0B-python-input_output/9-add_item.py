#!/usr/bin/python3
"""script that adds all arguments to a Python
list, and then save them to a file"""


import sys


save_to_json = __import__("7-save_to_json_file").save_to_json_file
load_from_json = __import__("8-load_from_json_file").load_from_json_file

argv = sys.argv[1:]
try:
    filename = "add_item.json"
    add_item = load_from_json(filename)
except:
    add_item = []
for arguments in argv:
    add_item.append(arguments)

save_to_json(add_item, filename)
