#!/usr/bin/python3
"""Define a module"""


def write_file(filename="", text=""):
    """define a function that write text into file"""

    with open(filename, 'w', encoding="utf-8") as file:
        contents = file.write(text)
        return contents
