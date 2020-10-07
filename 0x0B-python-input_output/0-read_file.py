#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename="", encoding="utf-8"):
    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename) as readFile:
        read_data = readFile.read()
        print(read_data, end="")
        readFile.closed
