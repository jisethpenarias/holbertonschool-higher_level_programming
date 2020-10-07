#!/usr/bin/python3
def read_file(filename=""):
    with open("my_file_0.txt") as readFile:
        for line in readFile:
            print(line, end="")
