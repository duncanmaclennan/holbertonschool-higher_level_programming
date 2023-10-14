#!/usr/bin/python3
"""
Function prints "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: str
        last_name: str

    Return:
        None

    Raises:
        TypeError: first/last name must be a string
    """
    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    print("My name is {0} {1}".format(first_name, last_name))
