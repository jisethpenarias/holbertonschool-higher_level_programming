#!/usr/bin/python3
"""
4-print_square module

The 4-print_square module supplies one function,
print_square(first_name, last_name).
"""


def print_square(size):
    """Public instance method that prints with the character #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    size = int(size)

    if size == 0:
        print("")
    else:
        for _ in range(size):
            for _ in range(size):
                print("#", end="")
            print("")
