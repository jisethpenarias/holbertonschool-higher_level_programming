#!/usr/bin/python3


def read_file(filename=""):
    with open(filename) as readFile:
        read_data = readFile.read()
        print(read_data, end="")
        readFile.closed
