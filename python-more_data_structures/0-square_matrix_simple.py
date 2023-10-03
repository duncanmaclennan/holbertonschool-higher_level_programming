#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix by squaring each element of the input matrix
    new_matrix = [[elem ** 2 for elem in row] for row in matrix]
    return new_matrix
