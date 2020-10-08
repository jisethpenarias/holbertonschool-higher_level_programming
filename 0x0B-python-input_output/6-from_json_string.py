#!/usr/bin/python3
"""returns an object represented by a JSON"""

import json


def from_json_string(my_str):
    """function that returns an object (Python data structure) represented
    by a JSON string"""
    # JSON(string) -> obj(struct)Python
    # Deserialize s((in this case my_str) a str instance containing a
    # JSON document) to a python object.
    return json.loads(my_str)
