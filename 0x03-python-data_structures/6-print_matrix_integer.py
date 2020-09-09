#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for axis1 in matrix:
        for idx, axis2 in enumerate(axis1):
            print("{:d}".format(axis2), end="" if idx == len(axis1) - 1 else " ")
        else:
            print("\n", end="")
