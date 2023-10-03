#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    # Ensure that tuple_a and tuple_b have at least two elements by filling with zeros if necessary
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Sum the first two elements of each tuple and return as a new tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
