#!/usr/bin/python3

import json


def from_json_string(my_str):
    """ returs a python data structure object represented by a JSON string"""
    obj = json.loads(my_str)
    return obj
