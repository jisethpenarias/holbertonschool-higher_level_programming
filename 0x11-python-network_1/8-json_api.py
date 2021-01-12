#!/usr/bin/python3
""" """

import requests
from sys import argv

if __name__ == "__main__":
    q = ""
    if len(argv) > 1:
        q = argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    jR = r.json()
    if bool(jR):
        print("[<{}>] <{}>".format(jR.get('id'), jR.get('name')))
    elif not bool(jR):
        print("No result")
    else:
        print("Not a valid JSON")
