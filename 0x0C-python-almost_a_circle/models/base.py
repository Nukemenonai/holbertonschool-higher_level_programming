#!/usr/bin/python3

import json

class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiates the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON representation of a list of dict """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON representation of list_objs to a file"""
        if list_objs is None:
            with open("{}.json".format(cls.__name__), 'w') as f:
                f.write("[]")
                f.close()
        else:
            json_list = []
            with open("{}.json".format(cls.__name__), 'w') as f:
                for item in list_objs:
                    json_list.append(item.to_dictionary())
                f.write(str(json_list))
                f.close()

    @staticmethod
    def from_json_string(json_string):
        """ Returns a list of the str repr json_string"""
        new_list = []
        if json_string is None or len(json_string) == 0:
            return new_list
        else:
            new_list = json.loads(json_string)
            return new_list

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes all set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
