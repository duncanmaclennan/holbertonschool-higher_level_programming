#!/usr/bin/python3
"""
class Base
"""
import json


class Base:
    """
    Creating Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises new Base instance

        Arg:
            id: int (optional)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        list_dict = []
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                jsonfile.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set
        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as jsonfile:
                dict_list = cls.from_json_string(jsonfile.read())
                return [cls.create(**dictionary) for dictionary in dict_list]
        except FileNotFoundError:
            return []
