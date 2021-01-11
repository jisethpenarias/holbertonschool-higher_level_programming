#!/usr/bin/python3
""" Error code:  script that takes in a URL, sends a request to
the URL and displays the body of the response. """


import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    status = response.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(response.text)
