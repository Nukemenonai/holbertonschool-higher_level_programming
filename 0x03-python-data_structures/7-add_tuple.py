#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a:
        tuple_a = (0, 0)
    if not tuple_b:
        tuple_b = (0, 0)
    if len(tuple_a) >= 0 and len(tuple_a) < 2:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) >= 0 and len(tuple_b) < 2:
        tuple_b = (tuple_b[0], 0)
    if len(tuple_a) > 2:
        tuple_a = tuple_a[0], tuple_a[1]
    if len(tuple_b) > 2:
        tuple_b = tuple_b[0], tuple_b[1]
    el_one = tuple_a[0] + tuple_b[0]
    el_two = tuple_a[1] + tuple_b[1]
    new_tup = (el_one, el_two)
    return new_tup
