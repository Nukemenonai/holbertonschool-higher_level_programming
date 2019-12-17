#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        tuple_a = (0, 0)
    elif tuple_b == ():
        tuple_b = (0, 0)
    elif len(tuple_a) > 2:
        tuple_a = tuple_a[0:2]
    elif len(tuple_b) > 2:
        tuple_b = tuple_b[0:2]
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    el_one = tuple_a[0] + tuple_b[0]
    el_two = tuple_a[1] + tuple_b[1]
    new_tup = (el_one, el_two)
    return new_tup
