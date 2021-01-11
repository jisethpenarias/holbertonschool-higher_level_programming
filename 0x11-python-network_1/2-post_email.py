#!/usr/bin/python3
""" POST an email: script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """

import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    email_value = urllib.parse.urlencode({'email': argv[2]})
    email_value = email_value.encode('ascii')
    url = argv[1]
    with urllib.request.urlopen(url, email_value) as response:
        resp = response.read().decode('utf-8')
    print(resp)
