#!/usr/bin/python3
"""
This module provides addition functionality.

It contains a function to add two numbers.
"""


def add_integer(a, b=98):
    """
    Add two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return a + b