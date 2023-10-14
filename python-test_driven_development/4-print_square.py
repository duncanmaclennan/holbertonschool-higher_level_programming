#!/usr/bin/python3
"""A module that print square"""


def print_square(size):
    """A function that print square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
