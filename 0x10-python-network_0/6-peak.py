#!/usr/bin/python3
"""
findpeak module
"""


def find_peak(list_of_integers):
    """ function to find the peak element in a list """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    else:
        peak = list_of_integers[0]
        for item in list_of_integers:
            if item > peak:
                peak = item
        return peak
