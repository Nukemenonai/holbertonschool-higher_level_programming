#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ reads n lines of a UTF8 file and prints to stdout"""

    lines = 0
    with open(filename, 'r') as f:
        count = len(open(filename).readlines())
        if nb_lines >= count or nb_lines <= 0:
            nb_lines = count
        for line in f:
            print(line, end="")
            lines += 1
            if lines == nb_lines:
                break
