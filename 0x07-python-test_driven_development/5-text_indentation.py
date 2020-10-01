#!/usr/bin/python3
"""
5-text_indentation module

The 5-text_indentation module supplies one function,
text_indentation(first_name, last_name).
"""


def text_indentation(text):
    """
    2 new lines after each of these characters: ., ? and :
    """
    i = 0
    if type(text) is not str:
        raise TypeError('text must be a string')
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n", end="")
            i += 1
            if i < len(text):
                while text[i] == " ":
                    i += 1
        else:
            i += 1
