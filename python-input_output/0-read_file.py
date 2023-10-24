#!/usr/bin/python3
"""
Function reads text file and prints to stdout
"""


def read_file(filename=""):
    """
    reads input file and prints to stdout
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
