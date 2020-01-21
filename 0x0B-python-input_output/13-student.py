#!/usr/bin/python3


class Student:
    """ defines a student by first name, last name and age """

    def __init__(self, first_name, last_name, age):
        """ Instantiates a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student"""
        if type(attrs) == list:
            new_dict = {}
            for item in attrs:
                if item in self.__dict__:
                    new_dict[item] = getattr(self, item)
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of a student instance"""
        for item in json:
            setattr(self, item, json[item])
