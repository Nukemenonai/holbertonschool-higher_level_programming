#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for item in new_list:
        if item == search:
            new_list[item] = replace
    return new_list
