#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """Define Base class init function"""
    __nb_objects = 0  # class var value is updated when instance var access it

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1  # access class var
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return str representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
