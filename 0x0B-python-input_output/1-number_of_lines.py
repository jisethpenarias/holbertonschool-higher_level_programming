#!/usr/bin/python3
"""defining a function that returns the number of lines in a file"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file"""

    number_lines = 0
    with open(filename) as file_opened:
        for line in file_opened:
            number_lines += 1
    return number_lines
