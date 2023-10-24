#!/usr/bin/python3
"""Define a module"""
import json


def load_from_json_file(filename):
    """Define a functoin that creates an Object from Json file"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
