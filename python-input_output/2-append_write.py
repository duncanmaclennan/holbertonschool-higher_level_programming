#!/usr/bin/python3
"""Define a module"""


def append_write(filename="", text=""):
    """Define a function that append text to file"""

    with open(filename, 'a', encoding="utf-8") as file:
        contents = file.write(text)
        return contents
