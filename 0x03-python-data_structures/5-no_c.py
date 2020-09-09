#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for letter in my_string:
        if letter != "c" and letter != "C":
            new_string += letter
            # concat a letter to the new_string
    return new_string
