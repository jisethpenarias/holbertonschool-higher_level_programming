#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """class MyList"""

    def print_sorted(self):
        """prints the list sorted"""
        print(sorted(self))
