#!/usr/bin/python3


def add_attribute(obj, attr, value):
    """  adds if possible an attribute to a class"""
    try:
        setattr(obj, attr, value)
    except:
        raise TypeError("can't add new attribute")
