#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function devides all elemens by a matrix"""

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    for sublists in matrix:
        if len(sublists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_sublist = []
        for item in sublists:
            if not isinstance(item, (int, float)):
                raise TypeError(err_msg)
            else:
                new_sublist.append(round(item / div, 2))
        new_matrix.append(new_sublist)

    return new_matrix
