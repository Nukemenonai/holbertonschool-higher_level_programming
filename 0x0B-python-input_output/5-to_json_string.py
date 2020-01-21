#!/usr/bin/python3

import json


def to_json_string(my_obj):
    """ returns the json representation of an object"""
    repr = json.dumps(my_obj)
    return repr
