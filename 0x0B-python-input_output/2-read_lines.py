#!/usr/bin/python3
"""read n number of lines from a file"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file (UTF8)
    and prints it to stdout"""

    with open(filename, encoding="utf-8") as file_opened:

        number_lines = 0
        for line in file_opened:
            number_lines += 1
            if (nb_lines <= 0) or (nb_lines >= number_lines):
                print(line, end='')
