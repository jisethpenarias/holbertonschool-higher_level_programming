#!/usr/bin/python3
def print_last_digit(number):
    lasDigit = (abs(number) % 10)
    print("{}".format(lasDigit), end="")
    return lasDigit
