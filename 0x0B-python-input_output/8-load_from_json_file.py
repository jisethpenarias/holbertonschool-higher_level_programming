#!/usr/bin/python3
"""Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""

    with open(filename, mode="r", encoding="utf-8") as file_opened:
        read_data = file_opened.read()
        # Deserialize s(a str instance containing a
        # JSON document) to a python object.
        # (file)JSON -> (obje)Python
        return json.loads(read_data)
