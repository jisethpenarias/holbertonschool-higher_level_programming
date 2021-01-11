#!/usr/bin/python3
""" POST and email: script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response. """

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value_email = argv[2]
    r = requests.post(url, data={'email': value_email})
    print(r.text)
