#!/usr/bin/python3
"""Define a module"""
import json


def save_to_json_file(my_obj, filename):
    """Define a functoin that write object to a text file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
