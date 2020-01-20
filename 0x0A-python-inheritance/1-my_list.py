#!/usr/bin/python3


class MyList(list):
    """ Class that inherits from list """

    def print_sorted(self):
        """prints a sorted copy of the instance MyList"""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
