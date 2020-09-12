#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    romanN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    intN = 0
    for i in range(len(roman_string)):
        if i > 0 and romanN[roman_string[i]] > romanN[roman_string[i - 1]]:
            intN += romanN[roman_string[i]] - (2 * romanN[roman_string[i - 1]])
        else:
            intN += romanN[roman_string[i]]
    return intN
