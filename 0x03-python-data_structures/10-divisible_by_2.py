#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    tof = []
    for number in my_list:
        tof += [number % 2 == 0]
    return tof
