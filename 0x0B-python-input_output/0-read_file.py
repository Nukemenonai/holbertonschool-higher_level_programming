#!/usr/bin/python3
def read_file(filename=""):
    """ reads a text file and prints it to stdout """

    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')
