#!/usr/bin/python3
""" Search API: script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv

if __name__ == "__main__":
    q = ""
    if len(argv) > 1:
        q = argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        jR = r.json()
        if jR:
            print("[{}] {}".format(jR.get('id'), jR.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
