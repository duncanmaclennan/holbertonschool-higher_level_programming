#!/usr/bin/python3
"""Base Class"""
import json
import os


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
        """Return Json str"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return Json dictionary"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that write list object to file in Json representation"""
        file_name = cls.__name__ + ".json"
        dict_list = []
        with open(file_name, "w") as file:  # file is a var for opened file
            if list_objs is None:
                file.write("[]")
            else:
                for item in list_objs:
                    # convert list instance to dict_list
                    dict_list.append(item.to_dictionary())
                    # convert dict_list to json string
                    # to_json_string is static, so use class to call
                file.write(Base.to_json_string(dict_list))

    @classmethod
    def create(cls, **dictionary):
        """Function that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_ins = cls(1, 2)
        else:
            new_ins = cls(1)
        new_ins.update(**dictionary)
        return new_ins

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""

        list_ins = []
        file_name = cls.__name__ + ".json"
        if not os.path.exists(file_name):
            return []
        else:
            # read Json file
            with open(file_name, "r") as file:
                # convert Json string to list of dict
                dict_list = cls.from_json_string(file.read())
                for item in dict_list:
                    # create new instance via reset value
                    list_ins.append(cls.create(**item))
        return list_ins
