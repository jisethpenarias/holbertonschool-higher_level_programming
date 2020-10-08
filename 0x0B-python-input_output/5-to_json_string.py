#!/usr/bin/python3
"""returns the JSON"""

import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    # the dumps on the json class serialize an object to a JSON
    # formatted string
    return json.dumps(my_obj)
