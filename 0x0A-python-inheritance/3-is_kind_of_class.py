#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """ true if an obj is an instance of
    or an instance of a class that inherits from a class
    """

    return isinstance(obj, a_class)
