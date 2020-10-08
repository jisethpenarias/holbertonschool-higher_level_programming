#!/usr/bin/python3
"""Saving object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using
    a JSON representation
    """

    with open(filename, mode="w", encoding="utf-8") as file_opened:
        # file_opened.write(json_obj) writes the contents of string
        # to the file, returning the number of characters written.
        # my object is encoded to JSON string
        # (my_obj)Python -> (string)JSON
        return file_opened.write(json.dumps(my_obj))
