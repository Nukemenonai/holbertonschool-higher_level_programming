#!/usr/bin/python3

import json


def load_from_json_file(filename):
    """ creates an object from a JSON file """
    with open(filename, 'r') as jf:
        my_obj = json.load(jf)
        jf.close()
        return my_obj
