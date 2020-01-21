#!/usr/bin/python3
def append_write(filename="", text=""):
    """ writes a string UTF8 to a text file
    returns the number of characters written
    filename: name of the file.
    text: the text to insert
    appends
    """

    with open(filename, 'a') as f:
        n = f.write(text)
        return n
