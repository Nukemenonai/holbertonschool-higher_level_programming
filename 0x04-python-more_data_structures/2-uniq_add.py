#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    new = list(set(my_list))
    for i in new:
        res += i
    return res
