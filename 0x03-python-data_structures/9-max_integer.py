#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = 0
    for number in my_list:
        if number > max_num:
            max_num = number
    return max_num
