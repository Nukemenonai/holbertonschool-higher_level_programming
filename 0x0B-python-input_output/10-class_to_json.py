#!/usr/bin/python3


def class_to_json(obj):
    """ returs dictionary description with simple data structure list
    for JSON serializaton of and object
    obj: is an instance of a Class
    """

    return obj.__dict__
