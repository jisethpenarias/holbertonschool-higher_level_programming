#!/usr/bin/python3
"""
2-matrix_divided module
The matrix_divided module function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """matrix_divided function that divides and return a new matrix."""

    new_matrix = []
    erro1 = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix) is 0:
        raise TypeError(erro1)

    for num_list in range(len(matrix)):
        if not isinstance(matrix[num_list], list):
            raise TypeError(erro1)
        elif len(matrix[0]) != len(matrix[num_list]):
            raise TypeError('Each row of the matrix must have the same size')
        new_row = []
        for number in matrix[num_list]:
            if not isinstance(number, (int, float)):
                raise TypeError(erro1)
            new_row.append(round(number/div, 2))
        new_matrix.append(new_row)
    return new_matrix
