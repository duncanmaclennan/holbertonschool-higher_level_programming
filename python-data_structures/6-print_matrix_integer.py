#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    # Iterate through each row in the matrix
    for row in matrix:
        # Initialize a string to store the row's elements
        row_string = ''

        # Iterate through each element in the row
        for i, element in enumerate(row):
            # Add the element to row_string, followed by a space if not the last element
            row_string += "{:d}".format(element)
            if i != len(row) - 1:
                row_string += " "

        # Print the row
        print(row_string)
