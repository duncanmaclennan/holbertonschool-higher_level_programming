#!/usr/bin/python3
"""Define a module"""
import json


def from_json_string(my_str):
    """Define a functoin that returns an object by a JSON string"""

    return json.loads(my_str)
