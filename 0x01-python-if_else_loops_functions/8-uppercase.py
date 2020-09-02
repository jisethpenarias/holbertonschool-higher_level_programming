#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) > 96 and ord(x) < 123:
                upper = ord(x) - 32
        else:
            upper = ord(x)
        print("{:c}".format(upper), end="")
    print("")
