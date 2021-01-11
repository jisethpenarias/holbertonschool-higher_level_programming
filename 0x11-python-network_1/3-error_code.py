#!/usr/bin/python3
""" Error code: script that takes in a URL,
sends a request to the URL and displays the body
of the response (decoded in utf-8). """

import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try: 
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error_code:
        print('Error code:', error_code.code)
