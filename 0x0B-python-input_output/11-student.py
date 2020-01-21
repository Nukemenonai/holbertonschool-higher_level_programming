#!/usr/bin/python3


class Student:
    """ defines a student by first name, last name and age """

    def __init__(self, first_name, last_name, age):
        """ Instantiates a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a student"""
        return self.__dict__
