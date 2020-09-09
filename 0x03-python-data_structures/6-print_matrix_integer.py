#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for axis1 in matrix:
        for axis2 in axis1:
            print("{}".format(axis2), end=" ")
        else:
            print("\n", end="")
