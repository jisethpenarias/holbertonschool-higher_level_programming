#!/usr/bin/python3
"""rewriting a file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) and
    returns the number of characters written"""

    with open(filename, mode="w", encoding="utf-8") as file_opened:
        s = str(text)
        # file_opened.write(s) writes the contents of string to the file,
        # returning the number of characters written.
        return file_opened.write(s)
