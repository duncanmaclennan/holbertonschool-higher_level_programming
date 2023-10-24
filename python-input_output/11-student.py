#!/usr/bin/python3
"""Define a student module"""


class Student:
    """Define a student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            return {k: val for k, val in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        for k, val in json.items():
            setattr(self, k, val)
