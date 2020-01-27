#!/usr/bin/python3

""" Base module """

import json
import csv

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

                string = cls.to_json_string(json_list)
                f.write(string)
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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        a_file = str(cls.__name__) + ".json"
        if not a_file:
            return []
        else:
            with open(a_file, encoding="utf-8") as f:
                instances = []
                ln = f.read()
                dictionary = cls.from_json_string(ln)
                for item in dictionary:
                    instances.append(cls.create(**item))
                return instances


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ """
        if list_objs is None:
            with open("{}.csv".format(cls.__name__), 'w') as f:
                f.write("[]")
                f.close()
        else:
            csv_list = []
            with open("{}.csv".format(cls.__name__), 'w') as f:
                for item in list_objs:
                    csv_list.append(item.to_dictionary().values())
                f.write("{}".format(csv_list))
                f.close()

    @classmethod
    def load_from_file_csv(cls):
        """ """
        a_file = cls.__name__ + ".csv"
        if not a_file:
            return []
        else:
            with open(a_file, encoding="utf-8") as f:
                c_instances = []
                ln = f.read()
                list1 = cls.to_dictionary(ln).values()
                for item in list1:
                    c_instance.append(cls.create(*item))
                return c_instances
