#!/usr/bin/python3
""" Define module"""


def inherits_from(obj, a_class):
    """ Definition of method of inherits_from"""

    if type(obj) is a_class:
        return False

    return isinstance(obj, a_class)
