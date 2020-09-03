#!/usr/bin/python3
for leter in range(122, 96, -1):
    print("{}".format(chr(leter) if leter % 2 == 0 else chr(leter-32)), end="")
