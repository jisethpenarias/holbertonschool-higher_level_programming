#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixSquared = list()
    for arr in matrix:
        matrixSquared.append(list(map(lambda number: number ** 2, arr)))
    return matrixSquared
