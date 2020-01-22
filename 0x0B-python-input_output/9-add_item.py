#!/usr/bin/python3

""" script that adds all arguments to a python list

This is the socumentation !!!

"""

import sys
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


""" script that adds all arguments to a python list

This is the socumentation !!!

"""


f = open("add_item.json", 'a')
f.close()
if len(open("add_item.json").readlines()) == 1:
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []
    save_to_json_file(my_list, "add_item.json")
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
    save_to_json_file(my_list, "add_item.json")
