#!/usr/bin/python3
def number_of_lines(filename=""):
    """ return the number of lines of a text file """
    lines = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
        f.close()
    return lines
