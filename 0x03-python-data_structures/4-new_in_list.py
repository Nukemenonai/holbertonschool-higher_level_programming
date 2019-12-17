#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cplist = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return cplist
    else:
        cplist[idx] = element
        return cplist
