#!/usr/bin/python3
"""writing to the end of a file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    and returns the number of characters added"""

    with open(filename, mode="a", encoding="utf-8") as file_opened:
        s = str(text)
        # file_opened.write(s) writes the contents of string to the file,
        # returning the number of characters written.
        return file_opened.write(s)
